import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.rcParams.update({
    'font.family': 'serif',
    'mathtext.fontset': 'cm',
    'font.size': 10,
    'axes.labelsize': 11,
    'axes.titlesize': 11
})

polito_navy = '#002B5B'
exam_red = '#B42828'
deep_teal = '#008080'
intuition_green = '#288250'

# =========================================================================
# 1. linear_plane_3d.pdf
# =========================================================================
np.random.seed(101)
N = 18
x1 = np.random.uniform(-2.0, 2.0, N)
x2 = np.random.uniform(-2.0, 2.0, N)
w1_true = 0.8
w2_true = -0.6
b_true = 1.2
noise = np.random.normal(0, 0.45, N)
y = w1_true * x1 + w2_true * x2 + b_true + noise

X1, X2 = np.meshgrid(np.linspace(-2.2, 2.2, 30), np.linspace(-2.2, 2.2, 30))
Y_plane = w1_true * X1 + w2_true * X2 + b_true

fig = plt.figure(figsize=(7.0, 5.5), dpi=300)
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X1, X2, Y_plane, cmap='YlGnBu', edgecolor='none', alpha=0.55, antialiased=True)
ax.plot_wireframe(X1, X2, Y_plane, color=polito_navy, alpha=0.18, rstride=3, cstride=3)

y_pred = w1_true * x1 + w2_true * x2 + b_true
for i in range(N):
    ax.plot([x1[i], x1[i]], [x2[i], x2[i]], [y[i], y_pred[i]], color=exam_red, lw=1.6, linestyle='--')

ax.scatter(x1, x2, y, color=exam_red, s=40, edgecolors='black', label=r'Observed Points $(\mathbf{x}_i, y_i)$', zorder=10)
ax.scatter(x1, x2, y_pred, color=polito_navy, s=25, alpha=0.6, label=r'Predictions $\hat{y}_i = \mathbf{w}^\top \mathbf{x}_i + b$')

idx = np.argmax(np.abs(noise))
ax.text(x1[idx]+0.2, x2[idx], (y[idx] + y_pred[idx])/2.0, 
        r'Residual $r_i = y_i - \hat{y}_i$', 
        color=exam_red, fontsize=9, fontweight='bold')

ax.view_init(elev=24, azim=-55)
ax.set_xlabel(r'Feature $X_1$', labelpad=-2)
ax.set_ylabel(r'Feature $X_2$', labelpad=-2)
ax.set_zlabel(r'Target $Y$', labelpad=-2)
ax.set_title('Linear Regression Hyperplane and Residual Orthogonal Drops', 
             pad=12, color=polito_navy, fontweight='bold', fontsize=11)
ax.tick_params(labelsize=8.5, pad=0)
ax.legend(loc='upper left', fontsize=8.5, framealpha=0.92)
plt.tight_layout()
plt.savefig('STUDY_GUIDE/figures/linear_plane_3d.pdf', bbox_inches='tight')
plt.close()
print('1. Saved linear_plane_3d.pdf')

# =========================================================================
# 2. gd_landscape_3panels.pdf
# =========================================================================
fig = plt.figure(figsize=(12.5, 3.8), dpi=300)
x = np.linspace(-2.2, 2.2, 100)
y_pts = np.linspace(-1.8, 1.8, 100)
X, Y = np.meshgrid(x, y_pts)
Z = X**2 + 2.0 * Y**2

ax1 = fig.add_subplot(131, projection='3d')
surf = ax1.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.88, antialiased=True)
ax1.view_init(elev=28, azim=-58)
ax1.set_xlabel(r'$w_1$', labelpad=-2)
ax1.set_ylabel(r'$w_2$', labelpad=-2)
ax1.set_zlabel(r'$f(w_1, w_2)$', labelpad=-2)
ax1.set_title('(a) 3D Loss Elevation Surface', pad=6, color=polito_navy, fontweight='bold')
ax1.tick_params(labelsize=8, pad=0)

ax2 = fig.add_subplot(132)
levels = [0.25, 0.8, 1.8, 3.2, 5.0, 7.5, 10.5]
cs = ax2.contour(X, Y, Z, levels=levels, colors=deep_teal, linewidths=1.2)
ax2.clabel(cs, inline=True, fontsize=7.5, fmt='%.1f')
ax2.contourf(X, Y, Z, levels=levels, cmap='YlGnBu_r', alpha=0.35)
ax2.plot(0, 0, marker='*', markersize=10, color=exam_red, label=r'Minimum $\mathbf{w}^* = (0,0)$')
ax2.set_xlabel(r'$w_1$')
ax2.set_ylabel(r'$w_2$')
ax2.set_title(r'(b) 2D Contour Map $f(\mathbf{w}) = c$', pad=8, color=polito_navy, fontweight='bold')
ax2.legend(loc='upper right', fontsize=8, framealpha=0.9)
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.set_aspect('equal', 'box')

ax3 = fig.add_subplot(133)
xq = np.linspace(-2.0, 2.0, 13)
yq = np.linspace(-1.6, 1.6, 11)
XQ, YQ = np.meshgrid(xq, yq)
U = 2.0 * XQ
V = 4.0 * YQ
N_grad = np.hypot(U, V)
N_grad[N_grad == 0] = 1.0
Un = U / N_grad
Vn = V / N_grad

ax3.contour(X, Y, Z, levels=levels, colors='gray', linewidths=0.7, alpha=0.45)
q = ax3.quiver(XQ, YQ, Un, Vn, N_grad, cmap='plasma', scale=22, width=0.0055, headwidth=4, headlength=5)
ax3.plot(0, 0, marker='*', markersize=10, color=exam_red)
ax3.set_xlabel(r'$w_1$')
ax3.set_ylabel(r'$w_2$')
ax3.set_title(r'(c) 2D Gradient Field $\nabla f(\mathbf{w})$', pad=8, color=polito_navy, fontweight='bold')
ax3.grid(True, linestyle=':', alpha=0.6)
ax3.set_aspect('equal', 'box')
cbar = fig.colorbar(q, ax=ax3, fraction=0.046, pad=0.04)
cbar.set_label(r'$\|\nabla f(\mathbf{w})\|$', fontsize=9)
cbar.ax.tick_params(labelsize=8)

plt.tight_layout()
plt.savefig('STUDY_GUIDE/figures/gd_landscape_3panels.pdf', bbox_inches='tight')
plt.close()
print('2. Saved gd_landscape_3panels.pdf')

# =========================================================================
# 3. gd_trajectories_initialization.pdf
# =========================================================================
def f_pot(x, y):
    return (x**2 - 1.2)**2 + 1.8 * y**2 + 0.3 * x * y

def grad_pot(x, y):
    df_dx = 2 * (x**2 - 1.2) * (2 * x) + 0.3 * y
    df_dy = 3.6 * y + 0.3 * x
    return df_dx, df_dy

x = np.linspace(-2.2, 2.2, 180)
y_pts = np.linspace(-1.8, 1.8, 150)
X, Y = np.meshgrid(x, y_pts)
Z = f_pot(X, Y)

fig, ax = plt.subplots(figsize=(6.4, 5.2), dpi=300)
levels = [0.1, 0.4, 0.9, 1.6, 2.5, 3.8, 5.5, 7.8, 10.5]
cs = ax.contour(X, Y, Z, levels=levels, colors='gray', linewidths=0.9, alpha=0.55)
ax.clabel(cs, inline=True, fontsize=7, fmt='%.1f')
ax.contourf(X, Y, Z, levels=levels, cmap='YlGnBu_r', alpha=0.25)

xq = np.linspace(-2.0, 2.0, 15)
yq = np.linspace(-1.6, 1.6, 13)
XQ, YQ = np.meshgrid(xq, yq)
UQ, VQ = grad_pot(XQ, YQ)
NQ = np.hypot(UQ, VQ)
NQ[NQ == 0] = 1.0
ax.quiver(XQ, YQ, -UQ/NQ, -VQ/NQ, color='#666666', scale=26, width=0.004, headwidth=4, headlength=5, alpha=0.6)

wA = [np.array([1.8, 1.3])]
lr = 0.08
for _ in range(45):
    cur = wA[-1]
    g = np.array(grad_pot(cur[0], cur[1]))
    wA.append(cur - lr * g)
wA = np.array(wA)

wB = [np.array([-0.2, -1.4])]
for _ in range(45):
    cur = wB[-1]
    g = np.array(grad_pot(cur[0], cur[1]))
    wB.append(cur - lr * g)
wB = np.array(wB)

ax.plot(wA[:, 0], wA[:, 1], color=polito_navy, lw=2.2, label=r'Trajectory $A$ ($\mathbf{w}^{(0)}_A \to \mathbf{w}^*_1$)')
ax.scatter(wA[:, 0], wA[:, 1], color=polito_navy, s=18, zorder=5)
ax.scatter(wA[0, 0], wA[0, 1], color=polito_navy, s=70, marker='o', edgecolors='black', zorder=6)
ax.annotate(r'$\mathbf{w}^{(0)}_A$', xy=(wA[0, 0], wA[0, 1]), xytext=(wA[0, 0]+0.1, wA[0, 1]+0.12),
            fontweight='bold', color=polito_navy, fontsize=10)

ax.plot(wB[:, 0], wB[:, 1], color=exam_red, lw=2.2, linestyle='--', label=r'Trajectory $B$ ($\mathbf{w}^{(0)}_B \to \mathbf{w}^*_2$)')
ax.scatter(wB[:, 0], wB[:, 1], color=exam_red, s=18, zorder=5)
ax.scatter(wB[0, 0], wB[0, 1], color=exam_red, s=70, marker='s', edgecolors='black', zorder=6)
ax.annotate(r'$\mathbf{w}^{(0)}_B$', xy=(wB[0, 0], wB[0, 1]), xytext=(wB[0, 0]-0.45, wB[0, 1]-0.15),
            fontweight='bold', color=exam_red, fontsize=10)

ax.plot(wA[-1, 0], wA[-1, 1], marker='*', markersize=12, color=intuition_green, zorder=7)
ax.annotate(r'Local Min 1 ($\mathbf{w}^*_1$)', xy=(wA[-1, 0], wA[-1, 1]), xytext=(wA[-1, 0]-0.3, wA[-1, 1]-0.25),
            fontweight='bold', color=intuition_green, fontsize=9)

ax.plot(wB[-1, 0], wB[-1, 1], marker='*', markersize=12, color=intuition_green, zorder=7)
ax.annotate(r'Local Min 2 ($\mathbf{w}^*_2$)', xy=(wB[-1, 0], wB[-1, 1]), xytext=(wB[-1, 0]-0.6, wB[-1, 1]+0.2),
            fontweight='bold', color=intuition_green, fontsize=9)

ax.plot(0, 0, marker='x', markersize=10, mew=2.5, color=exam_red, zorder=7)
ax.annotate(r'Saddle Point ($\nabla f = \mathbf{0}$)', xy=(0, 0), xytext=(-0.65, 0.25),
            fontweight='bold', color=exam_red, fontsize=9)

ax.set_xlabel(r'Parameter $w_1$')
ax.set_ylabel(r'Parameter $w_2$')
ax.set_title('Non-Convex Landscape: Stationary Points & Initialization Sensitivity', 
             pad=10, color=polito_navy, fontweight='bold', fontsize=10.5)
ax.legend(loc='upper left', fontsize=8.5, framealpha=0.92)
ax.grid(True, linestyle=':', alpha=0.5)
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-1.8, 1.8)
plt.tight_layout()
plt.savefig('STUDY_GUIDE/figures/gd_trajectories_initialization.pdf', bbox_inches='tight')
plt.close()
print('3. Saved gd_trajectories_initialization.pdf')

# =========================================================================
# 4. learning_rate_dynamics_contours.pdf
# =========================================================================
def f_el(x, y):
    return x**2 + 6.0 * y**2

def grad_el(x, y):
    return np.array([2.0 * x, 12.0 * y])

x = np.linspace(-3.2, 3.2, 200)
y_pts = np.linspace(-2.2, 2.2, 200)
X, Y = np.meshgrid(x, y_pts)
Z = f_el(X, Y)
levels = [0.4, 1.5, 3.5, 7.0, 12.0, 18.0, 26.0]

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(13.2, 4.0), dpi=300)

for ax in (ax1, ax2, ax3):
    ax.contour(X, Y, Z, levels=levels, colors='gray', linewidths=0.8, alpha=0.55)
    ax.contourf(X, Y, Z, levels=levels, cmap='YlGnBu_r', alpha=0.22)
    ax.plot(0, 0, marker='*', markersize=10, color=polito_navy)
    ax.set_xlabel(r'$w_1$')
    ax.set_ylabel(r'$w_2$')
    ax.grid(True, linestyle=':', alpha=0.45)
    ax.set_aspect('equal', 'box')
    ax.set_xlim(-3.2, 3.2)
    ax.set_ylim(-2.2, 2.2)

w0 = np.array([2.8, 1.6])
alpha_small = 0.02
traj_small = [w0]
for _ in range(18):
    traj_small.append(traj_small[-1] - alpha_small * grad_el(traj_small[-1][0], traj_small[-1][1]))
traj_small = np.array(traj_small)

ax1.plot(traj_small[:, 0], traj_small[:, 1], '-o', color=polito_navy, lw=1.8, markersize=3.5, label='Descent path')
ax1.plot(w0[0], w0[1], 's', color=polito_navy, markersize=7, label=r'Start $\mathbf{w}^{(0)}$')
ax1.set_title(r'(a) Under-stepping ($\alpha \ll \alpha_{\mathrm{opt}}$)' + '\nSlow crawling progress', 
              pad=8, color=polito_navy, fontweight='bold', fontsize=10)
ax1.legend(loc='lower left', fontsize=8)

w0_div = np.array([1.5, 0.45])
alpha_large = 0.175
traj_div = [w0_div]
for _ in range(7):
    traj_div.append(traj_div[-1] - alpha_large * grad_el(traj_div[-1][0], traj_div[-1][1]))
traj_div = np.array(traj_div)

ax2.plot(traj_div[:, 0], traj_div[:, 1], '-s', color=exam_red, lw=2.0, markersize=4, label='Oscillating path')
ax2.plot(w0_div[0], w0_div[1], 'o', color=polito_navy, markersize=7, label=r'Start $\mathbf{w}^{(0)}$')
ax2.set_title(r'(b) Overshooting ($\alpha > 2/\lambda_{\max}$)' + '\nOscillates and diverges', 
              pad=8, color=exam_red, fontweight='bold', fontsize=10)
ax2.legend(loc='lower left', fontsize=8)

w0_opt = np.array([2.6, 1.8])
traj_opt = [w0_opt]
for _ in range(5):
    cur = traj_opt[-1]
    g = grad_el(cur[0], cur[1])
    alpha_star = (g[0]*cur[0] + 6.0*g[1]*cur[1]) / (g[0]**2 + 6.0*g[1]**2)
    traj_opt.append(cur - alpha_star * g)
traj_opt = np.array(traj_opt)

ax3.plot(traj_opt[:, 0], traj_opt[:, 1], '-o', color=intuition_green, lw=2.2, markersize=5, label='Line search steps')
ax3.plot(w0_opt[0], w0_opt[1], 's', color=polito_navy, markersize=7, label=r'Start $\mathbf{w}^{(0)}$')

g0 = grad_el(w0_opt[0], w0_opt[1])
ray = np.array([w0_opt - t * g0 for t in np.linspace(-0.02, 0.12, 100)])
ax3.plot(ray[:, 0], ray[:, 1], ':', color=deep_teal, lw=1.5, alpha=0.8)

ax3.annotate(r'Tangent to isocurve:' + '\n' + r'$\langle \nabla f_{t+1}, \nabla f_t \rangle = 0$', 
             xy=(traj_opt[1, 0], traj_opt[1, 1]), 
             xytext=(traj_opt[1, 0]-2.7, traj_opt[1, 1]-1.1),
             arrowprops=dict(arrowstyle='->', color=deep_teal, lw=1.5),
             fontweight='bold', color=deep_teal, fontsize=8.5)

ax3.set_title(r'(c) Exact Line Search ($\alpha = \alpha^*$)' + '\nStep lands tangent to isocurve', 
              pad=8, color=intuition_green, fontweight='bold', fontsize=10)
ax3.legend(loc='lower left', fontsize=8)
plt.tight_layout()
plt.savefig('STUDY_GUIDE/figures/learning_rate_dynamics_contours.pdf', bbox_inches='tight')
plt.close()
print('4. Saved learning_rate_dynamics_contours.pdf')

# =========================================================================
# 5. cs231n_optimizer_comparison.pdf
# =========================================================================
def f_sad(x, y):
    return 1.0 * x**2 - 1.2 * y**2

def grad_sad(w):
    return np.array([2.0 * w[0], -2.4 * w[1]])

w_init = np.array([1.8, 0.05])

def run_sgd(w0, lr=0.08, steps=50):
    w = w0.copy()
    traj = [w.copy()]
    for _ in range(steps):
        w -= lr * grad_sad(w)
        traj.append(w.copy())
    return np.array(traj)

def run_momentum(w0, lr=0.04, beta=0.85, steps=50):
    w = w0.copy()
    v = np.zeros(2)
    traj = [w.copy()]
    for _ in range(steps):
        v = beta * v + lr * grad_sad(w)
        w -= v
        traj.append(w.copy())
    return np.array(traj)

def run_nag(w0, lr=0.04, beta=0.85, steps=50):
    w = w0.copy()
    v = np.zeros(2)
    traj = [w.copy()]
    for _ in range(steps):
        g = grad_sad(w - beta * v)
        v = beta * v + lr * g
        w -= v
        traj.append(w.copy())
    return np.array(traj)

def run_adagrad(w0, lr=0.35, eps=1e-8, steps=50):
    w = w0.copy()
    G = np.zeros(2)
    traj = [w.copy()]
    for _ in range(steps):
        g = grad_sad(w)
        G += g**2
        w -= (lr / (np.sqrt(G) + eps)) * g
        traj.append(w.copy())
    return np.array(traj)

def run_rmsprop(w0, lr=0.08, beta=0.9, eps=1e-8, steps=50):
    w = w0.copy()
    v = np.zeros(2)
    traj = [w.copy()]
    for _ in range(steps):
        g = grad_sad(w)
        v = beta * v + (1 - beta) * g**2
        w -= (lr / (np.sqrt(v) + eps)) * g
        traj.append(w.copy())
    return np.array(traj)

def run_adam(w0, lr=0.09, beta1=0.85, beta2=0.95, eps=1e-8, steps=50):
    w = w0.copy()
    m = np.zeros(2)
    v = np.zeros(2)
    traj = [w.copy()]
    for t in range(1, steps + 1):
        g = grad_sad(w)
        m = beta1 * m + (1 - beta1) * g
        v = beta2 * v + (1 - beta2) * g**2
        m_hat = m / (1 - beta1**t)
        v_hat = v / (1 - beta2**t)
        w -= (lr / (np.sqrt(v_hat) + eps)) * m_hat
        traj.append(w.copy())
    return np.array(traj)

traj_sgd = run_sgd(w_init)
traj_mom = run_momentum(w_init)
traj_nag = run_nag(w_init)
traj_adagrad = run_adagrad(w_init)
traj_rmsprop = run_rmsprop(w_init)
traj_adam = run_adam(w_init)

x = np.linspace(-2.2, 2.2, 200)
y_pts = np.linspace(-1.8, 1.8, 200)
X, Y = np.meshgrid(x, y_pts)
Z = f_sad(X, Y)

fig, ax = plt.subplots(figsize=(6.2, 5.0), dpi=300)
levels = np.linspace(-3.0, 3.0, 15)
cs = ax.contour(X, Y, Z, levels=levels, colors='gray', linewidths=0.75, alpha=0.5)
ax.contourf(X, Y, Z, levels=levels, cmap='coolwarm', alpha=0.20)

ax.plot(traj_sgd[:, 0], traj_sgd[:, 1], color='#333333', lw=1.8, label='SGD')
ax.plot(traj_mom[:, 0], traj_mom[:, 1], color='#288250', lw=2.0, label='Momentum')
ax.plot(traj_nag[:, 0], traj_nag[:, 1], color='#6A0DAD', lw=1.8, linestyle='-.', label='NAG')
ax.plot(traj_adagrad[:, 0], traj_adagrad[:, 1], color='#FF8C00', lw=1.8, linestyle=':', label='AdaGrad')
ax.plot(traj_rmsprop[:, 0], traj_rmsprop[:, 1], color='#B42828', lw=2.0, linestyle='--', label='RMSProp')
ax.plot(traj_adam[:, 0], traj_adam[:, 1], color='#002B5B', lw=2.2, label='Adam')

ax.plot(w_init[0], w_init[1], marker='o', markersize=8, color='#002B5B', zorder=10)
ax.annotate(r'Start $\mathbf{w}^{(0)}$', xy=(w_init[0], w_init[1]), xytext=(w_init[0]-0.6, w_init[1]+0.2),
            fontweight='bold', color='#002B5B', fontsize=9.5)

ax.plot(0, 0, marker='x', markersize=9, mew=2.5, color='#B42828', zorder=10)
ax.annotate(r'Saddle $(0,0)$', xy=(0, 0), xytext=(-0.5, -0.3),
            fontweight='bold', color='#B42828', fontsize=9)

ax.set_xlabel(r'Parameter $w_1$ (Positive Curvature $\lambda_1 > 0$)')
ax.set_ylabel(r'Parameter $w_2$ (Negative Curvature $\lambda_2 < 0$)')
ax.set_title('Optimizer Trajectories on Saddle Landscape', 
             pad=10, color='#002B5B', fontweight='bold', fontsize=10.5)
ax.legend(loc='lower left', fontsize=8.5, framealpha=0.92)
ax.grid(True, linestyle=':', alpha=0.5)
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-1.8, 1.8)
plt.tight_layout()
plt.savefig('STUDY_GUIDE/figures/cs231n_optimizer_comparison.pdf', bbox_inches='tight')
plt.close()
print('5. Saved cs231n_optimizer_comparison.pdf')

# =========================================================================
# 6. saddle_point_landscape.pdf
# =========================================================================
fig = plt.figure(figsize=(6.2, 5.0), dpi=300)
ax = fig.add_subplot(111, projection='3d')

w1 = np.linspace(-2.0, 2.0, 100)
w2 = np.linspace(-2.0, 2.0, 100)
W1, W2 = np.meshgrid(w1, w2)
Z = W1**2 - W2**2

surf = ax.plot_surface(W1, W2, Z, cmap='coolwarm', edgecolor='none', alpha=0.90, antialiased=True)
ax.view_init(elev=26, azim=-55)

w_slice = np.linspace(-2.0, 2.0, 100)
ax.plot(w_slice, np.zeros_like(w_slice), w_slice**2, color=polito_navy, lw=2.5, label=r'Upward curve ($\lambda_1 = +2$)')
ax.plot(np.zeros_like(w_slice), w_slice, -w_slice**2, color=exam_red, lw=2.5, label=r'Downward curve ($\lambda_2 = -2$)')
ax.scatter([0], [0], [0], color='black', s=60, marker='o', zorder=10)

ax.set_xlabel(r'$w_1$', labelpad=-2)
ax.set_ylabel(r'$w_2$', labelpad=-2)
ax.set_zlabel(r'$f(w_1, w_2) = w_1^2 - w_2^2$', labelpad=-2)
ax.set_title('3D Hyperbolic Saddle Surface: Mixed Curvature', 
             pad=10, color=polito_navy, fontweight='bold', fontsize=10.5)

ax.tick_params(labelsize=8.5, pad=0)
ax.legend(loc='upper right', fontsize=8.5, framealpha=0.92)
cbar = fig.colorbar(surf, ax=ax, shrink=0.62, aspect=14, pad=0.08)
cbar.set_label(r'Loss $f(w_1, w_2)$', fontsize=9.5)
cbar.ax.tick_params(labelsize=8)
plt.tight_layout()
plt.savefig('STUDY_GUIDE/figures/saddle_point_landscape.pdf', bbox_inches='tight')
plt.close()
print('6. Saved saddle_point_landscape.pdf')

# =========================================================================
# 7. sgd_oscillations_dynamics.pdf
# =========================================================================
def f_quad(x, y):
    return 0.5 * (x**2 + 5.0 * y**2)

def true_grad_quad(w):
    return np.array([w[0], 5.0 * w[1]])

np.random.seed(42)

w_bgd = np.array([2.8, 1.8])
traj_bgd = [w_bgd.copy()]
loss_bgd = [f_quad(w_bgd[0], w_bgd[1])]
lr = 0.15
for _ in range(60):
    g = true_grad_quad(w_bgd)
    w_bgd -= lr * g
    traj_bgd.append(w_bgd.copy())
    loss_bgd.append(f_quad(w_bgd[0], w_bgd[1]))
traj_bgd = np.array(traj_bgd)

w_sgd = np.array([2.8, 1.8])
traj_sgd = [w_sgd.copy()]
loss_sgd = [f_quad(w_sgd[0], w_sgd[1])]
noise_scale = 1.4
for _ in range(60):
    g = true_grad_quad(w_sgd) + np.random.normal(0, noise_scale, size=2)
    w_sgd -= lr * g
    traj_sgd.append(w_sgd.copy())
    loss_sgd.append(f_quad(w_sgd[0], w_sgd[1]))
traj_sgd = np.array(traj_sgd)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.0, 4.2), dpi=300)

x = np.linspace(-3.2, 3.2, 180)
y_pts = np.linspace(-2.2, 2.2, 180)
X, Y = np.meshgrid(x, y_pts)
Z = f_quad(X, Y)
levels = [0.2, 0.8, 2.0, 4.0, 7.5, 12.0, 18.0]

ax1.contour(X, Y, Z, levels=levels, colors='gray', linewidths=0.8, alpha=0.55)
ax1.contourf(X, Y, Z, levels=levels, cmap='YlGnBu_r', alpha=0.22)
ax1.plot(0, 0, marker='*', markersize=11, color=polito_navy)

ax1.plot(traj_bgd[:, 0], traj_bgd[:, 1], '-o', color=polito_navy, lw=2.0, markersize=3.5, label='Full Batch GD (Smooth)')
ax1.plot(traj_sgd[:, 0], traj_sgd[:, 1], '-s', color=exam_red, lw=1.6, markersize=3.0, alpha=0.85, label='Mini-Batch SGD (Noisy Walk)')
ax1.plot(2.8, 1.8, 'ko', markersize=6, label=r'Start $\mathbf{w}^{(0)}$')

ax1.set_xlabel(r'Parameter $w_1$')
ax1.set_ylabel(r'Parameter $w_2$')
ax1.set_title('(a) Contour Trajectory: Batch GD vs SGD', pad=8, color=polito_navy, fontweight='bold')
ax1.legend(loc='lower left', fontsize=8.5, framealpha=0.92)
ax1.grid(True, linestyle=':', alpha=0.45)
ax1.set_aspect('equal', 'box')
ax1.set_xlim(-3.2, 3.2)
ax1.set_ylim(-2.2, 2.2)

iters = np.arange(len(loss_bgd))
ax2.semilogy(iters, loss_bgd, color=polito_navy, lw=2.2, label='Full Batch GD (Monotonic Decay)')
ax2.semilogy(iters, loss_sgd, color=exam_red, lw=1.8, alpha=0.85, label='Mini-Batch SGD (Noise Floor)')

ax2.axhline(y=0.25, color=deep_teal, linestyle='--', lw=1.2, alpha=0.8)
ax2.annotate(r'Stochastic Noise Floor $\mathcal{O}(\eta/B)$', xy=(35, 0.25), xytext=(22, 1.5),
             arrowprops=dict(arrowstyle='->', color=deep_teal, lw=1.2),
             fontweight='bold', color=deep_teal, fontsize=8.5)

ax2.set_xlabel('Iteration / Epoch $t$')
ax2.set_ylabel(r'Objective Loss $\hat{\mathcal{R}}_N(\mathbf{w}_t)$ (Log Scale)')
ax2.set_title('(b) Convergence vs Persistent Variance Floor', pad=8, color=polito_navy, fontweight='bold')
ax2.legend(loc='lower left', fontsize=8.5, framealpha=0.92)
ax2.grid(True, linestyle=':', alpha=0.55, which='both')
ax2.set_xlim(0, 58)

plt.tight_layout()
plt.savefig('STUDY_GUIDE/figures/sgd_oscillations_dynamics.pdf', bbox_inches='tight')
plt.close()
print('7. Saved sgd_oscillations_dynamics.pdf')
