def summarize(text: str, tokenizer, model) -> str:
    input_ids = tokenizer.prepare_seq2seq_batch(
        [text],
        src_lang="en_XX",  # fairseq training artifact
        return_tensors="pt",
        padding="max_length",
        truncation=True,
        max_length=600
    )["input_ids"]

    output_ids = model.generate(
        input_ids=input_ids,
        max_length=162,
        no_repeat_ngram_size=3,
        num_beams=5,
        top_k=0
    )[0]

    summary = tokenizer.decode(output_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)
    return summary
