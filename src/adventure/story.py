from adventure.utils import read_events_from_file
import random
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text

console = Console()

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "You stand still, unsure what to do. The forest swallows you."

def left_path(event):
    return f"[bold green]You walk left.[/bold green] {event}"

def right_path(event):
    return f"[bold cyan]You walk right.[/bold cyan] {event}"

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    # Intro panel
    console.print(Panel.fit(
        "[bold yellow]You wake up in a dark forest.[/bold yellow]\nYou can go [green]left[/green] or [cyan]right[/cyan].",
        title="🌲 Adventure Begins 🌲",
        border_style="bold magenta"
    ))

    while True:
        choice = Prompt.ask("\n[bold white]Which direction do you choose?[/bold white]", choices=["left", "right", "exit"])
        if choice == "exit":
            console.print("\n[bold red]You decide to rest and end your journey. Goodbye[/bold red]")
            break
        
        result = step(choice, events)
        console.print(result)
