import numpy as np
import pandas as pd
import os

df=pd.read_csv(os.path.join(os.path.dirname(__file__), "orthogonal_polynomials.csv"), index_col=["p_n(x)", "n", "i"])

def f(x):
    return np.cos(x)

target_data=df.loc["P_n(x)", 10]

x_i=target_data["x_i"].values
w_i=target_data["w_i"].values

gauss_result=np.sum(w_i*f(x_i))
exact_result=2*np.sin(1)

print(f"ガウス積分の結果:{gauss_result:.10f}")
print(f"真の値:{exact_result:.10f}")