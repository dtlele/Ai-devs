**Modification to calculate RSI correctly**

Since the current implementation simply returns a list of 50s, we'll update it to calculate the Relative Strength Index (RSI) correctly. We'll use the Williams' Percent Range formula.

```diff
--- a/indicators/rsi.py
+++ b/indicators/rsi.py

def calculate_rsi(prices):
-    return [50] * len(prices)
+    delta = []
+    gain, loss = [], []

+    for i in range(len(prices)):
+        if i == 0:
+            continue
+        current = prices[i]
+        previous = prices[i - 1]
+        gain.append(max(0, current - previous))
+        loss.append(min(0, current - previous))

+    avg_gain = sum(gain) / len(gain)
+    avg_loss = sum(loss) / len(loss)

+    rs = avg_gain / avg_loss if avg_loss != 0 else 1
+    rsi = 100.0 - (100.0 / (1 + rs))
+
+    return [round(rsi, 2) for _ in prices]
```

**Note:**

* This modification assumes the input `prices` is a list of floats representing price changes.
* The RSI calculation follows the Williams' Percent Range formula.
* I added some intermediate variables to make the code more readable.