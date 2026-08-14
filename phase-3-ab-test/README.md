# A/B Test Simulator

A simulation and analysis of an A/B test, investigating how sample size affects a hypothesis test's ability to detect a real difference between two versions.

## What it does

Simulates two webpage versions with different true click-through rates (10% vs 12%), then runs a two-proportion z-test to check whether the observed difference is statistically significant. Repeats this across a range of sample sizes (100 to 50,000 visitors per group) to visualize how statistical power changes with sample size.

## Usage

Open ab_test_simulator.ipynb in VS Code (with the Jupyter extension) or Jupyter itself, and run all cells in order.

## Key finding

The same real 2-percentage-point gap between the two versions went from statistically undetectable (p > 0.05) at small sample sizes to overwhelmingly significant (p < 10^-17) at large sample sizes, even though the underlying true rates never changed. This demonstrates that failing to detect a difference with a small sample doesn't mean no real difference exists - it may just mean there wasn't enough data.

## What I learned
- What a hypothesis test actually answers: is an observed difference likely real, or explainable by random chance
- The z-statistic (standardized distance between two rates) and p-value (probability of the observed gap under the assumption of no real difference)
- Why small samples struggle to distinguish real effects from noise, and why the same true effect becomes obvious with enough data - this is what statistical power means
- Working in Jupyter notebooks inside VS Code, including selecting the correct kernel/virtual environment
- np.random.seed() only affects the sequence of random calls that immediately follow it, not every future random call in a session
- Using a log scale for visualizing values spanning many orders of magnitude
- Writing markdown cells alongside code to produce a genuinely readable, standalone analysis notebook