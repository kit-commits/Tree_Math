# Tree_Math

Use critical thinking to estimate **when a tree fell**:

1. Record when you heard the tree crash.
2. Estimate your distance from the tree.
3. Convert distance to sound delay using the speed of sound (343 m/s).
4. Subtract that delay from the heard time.

Formula:

`fall_time = heard_time - (distance_meters / 343)`

This repository includes a small calculator script:

```bash
python tree_fall_time.py \
  --heard-time "2026-06-08T10:00:00" \
  --distance-meters 686
```

Expected output:

`Estimated tree fall time: 2026-06-08T09:59:58`
