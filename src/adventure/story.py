from adventure.utils import read_events_from_file
import random
from rich.console import Console
from rich.panel import Panel

console = Console()

default_message = "You stand still, unsure what to do. The forest swallows you."

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "exit":
        return "Goodbye!"
    if choice == "left":
        return f"[bold green]You walk left.[/bold green] {random_event}"
    elif choice == "right":
        return f"[bold cyan]You walk right.[/bold cyan] {random_event}"
    else:
        return default_message

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    # Intro panel
    console.print(Panel.fit(
        "[bold yellow]You wake up in a dark forest.[/bold yellow]\nYou can go [green]left[/green] or [cyan]right[/cyan].",
        title="Adventure Begins",
        border_style="bold magenta"
    ))

    while True:
        # Use plain input for maximum test compatibility
        choice = input("\nWhich direction do you choose? (left/right/exit): ").strip().lower()
        if choice not in ["left", "right", "exit"]:
            console.print("Invalid choice. Please type left, right, or exit.")
            continue

        result = step(choice, events)

        # Rich output for paths
        if choice in ["left", "right"]:
            console.print(result)
        elif choice == "exit":
            # Print immediately after prompt line
            print(result)
            break
