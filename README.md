# hello-cprofile
playground of cProfile

## How to run

```shell
python -m cProfile -o hello.py.profile hello.py
python analyze.py hello.py.profile
```

## Results

``shell
$ python analyze.py hello.py.profile
['analyze.py', 'hello.py.profile']
Mon Dec 14 21:28:41 2020    hello.py.profile

         34 function calls in 10.030 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       10   10.030    1.003   10.030    1.003 {built-in method time.sleep}
       10    0.000    0.000    0.000    0.000 {built-in method builtins.print}
       10    0.000    0.000   10.030    1.003 hello.py:4(sleep_)
        1    0.000    0.000   10.030   10.030 hello.py:8(main)
        1    0.000    0.000   10.030   10.030 hello.py:1(<module>)
        1    0.000    0.000   10.030   10.030 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}.sort_stats(SortKey.TIME).print_stats(10)
```
