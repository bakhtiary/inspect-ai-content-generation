## inspect-ai-content-generation

## requirements

* uv

## running

```bash
uv sync
uv run jupyter notebook
```

The result of the current run can be seen with:

```bash
inspect view --log-dir ./logs
```

## next steps:

I have introduced the Evaluation class. Right now this concept only holds the dataset and 
the way the setup will be scored. I am ok with undoing this because maybe for the evaluation we should 
rely completely on the inspect-ai framework concepts for now. 

The solver should be mostly implemented with our own code. I am thinking the current "implementation" would be challenging 
to debug in production. Especially the LLM calls need to be monitored, and managed.

The next first thing I would do is ask what the use case of this is, is it realtime, or batch. What cost constraints and time
limits do we have? 

I would also ask for some existing copies, with human scores for quality. This would allow me to test any LLM judges that
we may add.

For the evaluation I would add more samples of what we want and what we don't want. Ideally, I would check for

* All important information are included.
* Nothing hallucinated is included.
* The details that need to be removed are correctly excluded.
* The tone of the listing corresponds to the qualities that we want (serious/fun, emojis/or no emojis)
* We can thwart prompt hijacking

I'd say 10 samples for each category is good enough