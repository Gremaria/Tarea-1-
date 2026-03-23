import time
from typing import List, Dict, Any

from io_handler import (
    load_tasks,
    load_resources,
    show_results,
    show_schedule,
    save_schedule
)

from scheduler import (
    generate_schedule,
    compute_metrics
)


def main() -> None:
    tasks: List[Dict[str, Any]] = load_tasks()
    resources: List[Dict[str, Any]] = load_resources()

    start_time: float = time.time()

    schedule: List[Dict[str, Any]] = generate_schedule(tasks, resources)
    metrics: Dict[str, Any] = compute_metrics(schedule, tasks)

    end_time: float = time.time()
    execution_time_ms: float = (end_time - start_time) * 1000

    show_results(metrics, execution_time_ms)
    show_schedule(schedule)

    save_option: str = input("\n¿Guardar cronograma? (s/n): ").strip().lower()

    if save_option == "s":
        save_schedule(schedule)


if __name__ == "__main__":
    main()