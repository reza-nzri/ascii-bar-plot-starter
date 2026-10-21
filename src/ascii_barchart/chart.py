from rich.console import Console
from rich.text import Text

STYLES = {
    "A": "bold cyan",
    "B": "bold magenta",
    "C": "bold green",
    "D": "bold yellow",
}


def scale_bar(value, maximum, width=40):
    if maximum <= 0:
        return 0
    return round(value / maximum * width)


def render_bar_chart(values, width=40):
    console = Console()
    if not values:
        return

    maximum = max(value for _, value in values)
    for category, value in values:
        length = scale_bar(value, maximum, width)
        line = Text(f"{category} | ")
        line.append("█" * length, style=STYLES.get(category, "white"))
        line.append(f" {value:.2f}")
        console.print(line)
