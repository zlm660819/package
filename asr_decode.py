#ctc predix beam search
def _prefix_beam_decode(y, beam_size, blank):
    T, V = y.shape
    log_y = np.log(y)
    beam = [(tuple(), (0, ninf))]

    for t in range(T):
        new_beam = defaultdict(lambda: (ninf, ninf))
        for prefix, (p_b, p_nb) in beam:
            for i in range(V):
                p = log_y[t, i]
                if i == blank:
                    new_p_b, new_p_nb = new_beam[prefix]
                    new_p_b = logsumexp(new_p_b, p_b + p, p_nb + p)
                    new_beam[prefix] = (new_p_b, new_p_nb)
                    continue
                end_t = prefix[-1] if prefix else None
                # 判断之前beam项中的最后一个元素和i的元素是不是一样
                new_prefix = prefix + (i,)
                new_p_b, new_p_nb = new_beam[new_prefix]
                # 如果不一样，则将i这项加入路径中
                if i != end_t:
                    new_p_nb = logsumexp(new_p_nb, p_b + p, p_nb + p)
                else:
                    new_p_nb = logsumexp(new_p_nb, p_b + p)
                new_beam[new_prefix] = (new_p_b, new_p_nb)
                # 如果一样，保留现有的路径，但是概率上要加上新的这个i项的概率
                if i == end_t:
                    new_p_b, new_p_nb = new_beam[prefix]
                    new_p_nb = logsumexp(new_p_nb, p_nb + p)
                    new_beam[prefix] = (new_p_b, new_p_nb)

        # 选取最优的beam_size个路径
        beam = sorted(new_beam.items(), key=lambda x: logsumexp(*x[1]), reverse=True)
        beam = beam[:beam_size]
    return beam
  
 #rnnt beam search
def default_beam_search(self, h: torch.Tensor) -> List[Hypothesis]:
    """Beam search implementation.
       Args:
            x: Encoded speech features (T_max, D_enc)
       Returns:
            nbest_hyps: N-best decoding results
    """
    beam = min(self.beam_size, self.vocab_size)
    beam_k = min(beam, (self.vocab_size - 1))

    init_tensor = h.unsqueeze(0)
    blank_tensor = init_tensor.new_zeros(1, dtype=torch.long)
    dec_state = self.decoder.init_state(init_tensor)
    kept_hyps = [Hypothesis(score=0.0, yseq=[self.blank], dec_state=dec_state)]
    cache = {}

    for hi in h:
        hyps = kept_hyps
        kept_hyps = []
        while True:
            max_hyp = max(hyps, key=lambda x: x.score)
            hyps.remove(max_hyp)

            y, state, lm_tokens = self.decoder.score(max_hyp, cache, init_tensor)
            ytu = torch.log_softmax(self.decoder.joint_network(hi, y[0]), dim=-1)
            top_k = ytu[1:].topk(beam_k, dim=-1)
            ytu = (torch.cat((top_k[0], ytu[0:1])), torch.cat((top_k[1] + 1, blank_tensor)),)
            
            if self.lm:
               lm_state, lm_scores = self.lm.predict(max_hyp.lm_state, lm_tokens)
            for logp, k in zip(*ytu):
                new_hyp = Hypothesis(
                score=(max_hyp.score + float(logp)),
                      yseq=max_hyp.yseq[:],
                      dec_state=max_hyp.dec_state,
                      lm_state=max_hyp.lm_state,
                      )

                 if k == self.blank:
                      kept_hyps.append(new_hyp)
                 else:
                     new_hyp.dec_state = state
                     new_hyp.yseq.append(int(k))
                     if self.lm:
                         new_hyp.lm_state = lm_state
                         new_hyp.score += self.lm_weight * lm_scores[0][k]
                 hyps.append(new_hyp)

            hyps_max = float(max(hyps, key=lambda x: x.score).score)
            kept_most_prob = sorted(
                  [hyp for hyp in kept_hyps if hyp.score > hyps_max],
                 key=lambda x: x.score,
              )
            if len(kept_most_prob) >= beam:
                kept_hyps = kept_most_prob
                break

     return self.sort_nbest(kept_hyps)
