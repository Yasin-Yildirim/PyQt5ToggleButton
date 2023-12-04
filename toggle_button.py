from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class ToggleButton(QCheckBox):
    """
    Custom toggle button that inherits from QCheckBox.
    It displays a sliding circle indicator to represent the checked/unchecked state.
    """

    def __init__(self, parent=None, bg_color="#777", circle_color="#DDD",
                 active_color="#00BCFF", animation_curve=QEasingCurve.OutBounce):
        """
        Initialize the toggle button with optional background color, circle color,
        active color, and the animation curve.
        """
        super().__init__(parent)

        # Set the cursor to a pointing hand to indicate this widget is clickable.
        self.setCursor(Qt.PointingHandCursor)

        # Initialize the colors for the button's states.
        self._bg_color = bg_color
        self._circle_color = circle_color
        self._active_color = active_color

        # Calculate the initial circle position based on the width of the widget.
        self._circle_position = self.width() // 20

        # Set up the animation for the circle sliding effect.
        self.animation = QPropertyAnimation(self, b"circle_position", self)
        self.animation.setEasingCurve(animation_curve)
        self.animation.setDuration(500)

        # Connect the stateChanged signal to start the transition animation.
        self.stateChanged.connect(self.start_transition)

        # Debug print statement to check the width during initialization.
        print(f"width: {self.width()}")

    @pyqtProperty(int)
    def circle_position(self):
        """
        Property that holds the current position of the circle indicator.
        """
        return self._circle_position

    @circle_position.setter
    def circle_position(self, pos):
        """
        Setter for the circle_position property. Updates the widget whenever the position changes.
        """
        print(f"position: {self._circle_position}")
        self._circle_position = pos
        self.update()

    def start_transition(self, value):
        """
        Start the animation transition when the toggle state changes.
        """
        self.animation.stop()
        # Determine the new end value for the animation based on the toggle state.
        if value:
            self.animation.setEndValue(self.width() - (self.width() // 3 + self.width() // 20))
        else:
            self.animation.setEndValue(self.width() // 20)

        # Start the animation.
        self.animation.start()

    def hitButton(self, pos: QPoint):
        """
        Determine if the given position is within the clickable area of the widget.
        """
        return self.contentsRect().contains(pos)

    def paintEvent(self, e):
        """
        Paint the toggle button with the appropriate colors and positions for the circle indicator.
        """
        print(f"circle positions: {self._circle_position}")
        print(f"width: {self.width()}")
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        p.setPen(Qt.NoPen)

        # Draw the background rectangle.
        rect = QRect(0, 0, self.width(), self.height())
        if not self.isChecked():
            p.setBrush(QColor(self._bg_color))
            p.drawRoundedRect(0, 0, rect.width(), self.height(), self.height() / 2, self.height() / 2)

            # Draw the circle in the off position.
            p.setBrush(QColor(self._circle_color))
            p.drawEllipse(self._circle_position, self.height() // 10, self.width() // 3, int(self.height() * 0.8))
        else:
            # Draw the background rectangle in the active color.
            p.setBrush(QColor(self._active_color))
            p.drawRoundedRect(0, 0, rect.width(), self.height(), self.height() / 2, self.height() / 2)

            # Draw the circle in the on position.
            p.setBrush(QColor(self._circle_color))
            p.drawEllipse(self._circle_position, self.height() // 10, self.width() // 3, int(self.height() * 0.8))

        # End the painting.
        p.end()

    def resizeEvent(self, event):
        """
        Handle the resize event to update the circle position and animation values accordingly.
        """
        super().resizeEvent(event)
        # Recalculate the circle position based on the new width.
        self._circle_position = self.width() // 20
        # Update the end value of the animation based on the current state and width.
        if self.isChecked():
            self.animation.setEndValue(self.width() - (self.width() // 3 + self.width() // 20))
        else:
            self.animation.setEndValue(self.width() // 20)
        self.update()

