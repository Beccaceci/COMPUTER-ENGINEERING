#!/usr/bin/env python3
"""
saddle_point_landscape.py — 3Blue1Brown Style 3D Loss Landscape & Saddle Point Visualization
Demonstrates Dauphin et al. (2014) & Goodfellow et al. (2016) Figure 4.4 / 4.5 using Manim.
"""
from manim import *

class SaddlePointScene(ThreeDScene):
    def construct(self):
        # 3Blue1Brown Dark Aesthetic
        self.camera.background_color = "#0f0f14"

        # 3D Axes
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-4, 4, 2],
            x_length=6,
            y_length=6,
            z_length=5
        )

        # Non-convex Saddle Surface: f(w1, w2) = w1^2 - w2^2
        saddle = Surface(
            lambda u, v: axes.c2p(u, v, (u**2 - v**2) * 0.4),
            u_range=[-2.5, 2.5],
            v_range=[-2.5, 2.5],
            resolution=(40, 40),
            should_make_jagged=False
        )
        saddle.set_style(
            fill_opacity=0.85,
            stroke_color=BLUE_D,
            stroke_width=0.5
        )
        saddle.set_fill_by_value(
            axes=axes,
            colors=[(RED_D, -2.5), (YELLOW_D, 0), (TEAL_D, 2.5)],
            axis=2
        )

        # Set 3B1B Camera Orientation
        self.set_camera_orientation(phi=65 * DEGREES, theta=-45 * DEGREES)

        # Title Label in 2D Screen Space
        title = Text("High-Dimensional Saddle Point & Curvature", font_size=32, color=YELLOW_C)
        subtitle = Text(r"$\mathbf{H} = \nabla^2 f(\mathbf{w})$ has mixed eigenvalues: $\lambda_1 > 0, \lambda_2 < 0$", font_size=22, color=GRAY_A)
        subtitle.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(title, subtitle)
        title.to_corner(UL)
        subtitle.to_corner(UL).shift(DOWN * 0.6)

        # Stationary Saddle Point
        saddle_point = Dot3D(point=axes.c2p(0, 0, 0), radius=0.15, color=RED_C)
        saddle_label = Text("Saddle Point: ∇f = 0", font_size=20, color=RED_C)
        self.add_fixed_in_frame_mobjects(saddle_label)
        saddle_label.next_to(axes.c2p(0, 0, 0), UP).shift(UP * 0.5)

        self.add(axes, saddle, saddle_point)
