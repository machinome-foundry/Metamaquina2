"""Independent old-law parity for the X and Y belt pulley angles."""

import math
import re

from machinome.core.expressions import parse, render
from solid2 import get_animation_time

from simulation.x_stage import x_belt
from simulation.y_axis import y_belt


def evaluate(expression, time):
    """Evaluate the arithmetic Solid2 expression at one animation time."""
    source = render(parse(str(expression))).replace('$t', repr(time))
    source = re.sub(r'\bfloor\(', 'FLOOR(', source)
    return eval(source, {'__builtins__': {}}, {'FLOOR': math.floor})


def old_x(position):
    anchor = ((position - x_belt.CLAMP_ORIGIN)
              * x_belt.gt2.span_scale(x_belt.CIRCLES, x_belt.CLAMP_SPAN))
    return (math.degrees(x_belt.PULLEY_PHASE)
            - math.degrees(anchor /
                           (x_belt.PULLEY_RADIUS + x_belt.gt2.PITCH_LINE)))


def old_y(position):
    anchor = ((position - y_belt.CLAMP_ORIGIN)
              * y_belt.gt2.span_scale(y_belt.CIRCLES, y_belt.CLAMP_SPAN))
    gone = (y_belt.STATIONS[2 * y_belt.CLAMP_SPAN] + anchor
            - y_belt.STATIONS[y_belt.PULLEY_ARC])
    return (math.degrees(y_belt.PULLEY_PHASE)
            + math.degrees(gone /
                           (y_belt.PULLEY_RADIUS + y_belt.gt2.PITCH_LINE)))


positions = (-400.0, -100.0, 0.0, 100.0, 400.0)
for name, function, legacy in (
        ('x', x_belt.pulley_angle, old_x),
        ('y', y_belt.pulley_angle, old_y)):
    values = []
    for position in positions:
        actual, expected = function(position), legacy(position)
        assert math.isclose(actual, expected, rel_tol=0.0, abs_tol=1e-12), (
            name, position, expected, actual)
        values.append(actual)
    assert max(values) - min(values) > 720  # signed travel stays unwrapped
    print(name, 'numeric parity', values)

time = get_animation_time()
for name, expression, legacy in (
        ('x', x_belt.pulley_angle(time), old_x),
        ('y', y_belt.pulley_angle(time), old_y)):
    for value in (-400.0, -100.0, 0.0, 100.0, 400.0):
        actual, expected = evaluate(expression, value), legacy(value)
        assert math.isclose(actual, expected, rel_tol=0.0, abs_tol=1e-10), (
            name, value, expected, actual)
    print(name, 'Solid2 evaluated parity', expression)
