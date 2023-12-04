# PyQt5ToggleButton
Toggle button with PyQt5

ToggleButton Widget
Overview
ToggleButton is a custom widget for PyQt5, extending QCheckBox. It provides a visually appealing toggle switch with a sliding circle indicator. This widget is designed to be a drop-in replacement for standard checkboxes, offering a more interactive user interface element for toggling states.

Features
Customizable colors for background, active state, and circle indicator.
Smooth animation transition for the circle indicator.
Easy integration with existing PyQt5 applications.

Installation
To use the ToggleButton widget in your PyQt5 application, simply include the toggle_button.py file in your project directory.

Usage
To use the ToggleButton in your PyQt5 application, you can import and add it to your layout just like any standard PyQt widget.

from toggle_button import ToggleButton

# Initialize the toggle button
toggle_btn = ToggleButton()

# Optionally, set custom colors and properties
toggle_btn.set_bg_color("#444")
toggle_btn.set_circle_color("#FFF")
toggle_btn.set_active_color("#0F0")

# Add it to your layout
layout.addWidget(toggle_btn)

Customization
You can customize the ToggleButton by changing its background color, circle color, and the color when activated. These can be set during initialization or by using the respective setter methods.

Requirements
PyQt5
