import json

from medilink_contract import build_summary


def main() -> None:
    patient = {
        "patient_id": "P-1001",
        "name": "Maria Santos",
        "age": 42,
        "care_plan": "Primary Care",
    }

    appointments = [
        {
            "appointment_id": "A-201",
            "doctor": "Dr. Lee",
            "time": "2026-10-07T09:00:00",
            "status": "confirmed",
        },
        {
            "appointment_id": "A-202",
            "doctor": "Dr. Chen",
            "time": "2026-10-14T14:30:00",
            "status": "scheduled",
        },
    ]

    summary = build_summary(patient, appointments)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
