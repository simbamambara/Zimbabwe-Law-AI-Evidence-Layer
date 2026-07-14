# Data Directory

I use this directory to separate source evidence from the derivatives I create from it.

- `raw/` contains the rebuilt source dataset that I treat as immutable evidence.
- `processed/` contains reproducible derivatives created through the normalisation pipeline.
- `public/` contains minimised derivatives that still require approval before release.
- `index/` contains review-friendly indexes.
- `metadata/` contains validation reports, manifests, queues, hashes, and audit evidence.

I do not edit the JSONL datasets manually. When I find an error, I correct the source process or normalisation code and rebuild the affected outputs so that the change remains traceable.