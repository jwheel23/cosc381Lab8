from adventure.utils import read_events_from_file
import random
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

console = Console()

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "exit":
        # Return a plain string for auto-tests
        return "Goodbye!"
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
        title="Adventure Begins",
        border_style="bold magenta"
    ))

    while True:
        # Prompt for user choice
        choice = Prompt.ask("\n[bold white]Which direction do you choose?[/bold white]", choices=["left", "right", "exit"])

        result = step(choice, events)

        # Print Rich-styled output for normal paths
        if choice in ["left", "right"]:
            console.print(result)
        # Print plain goodbye for exit so test captures it
        elif choice == "exit":
            print(result)  
            break
