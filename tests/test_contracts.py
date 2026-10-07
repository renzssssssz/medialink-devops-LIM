import unittest

from medilink_contract import build_summary


class BuildSummaryContractTests(unittest.TestCase):
    def test_summary_preserves_required_public_contract(self):
        patient = {"patient_id": "P-1001", "name": "Maria Santos"}
        appointments = [{"appointment_id": "A-201"}]

        summary = build_summary(patient, appointments, "maintenance")

        self.assertIn("patient", summary)
        self.assertIn("appointments", summary)
        self.assertIn("clinic_status", summary)
        self.assertEqual(summary["clinic_status"], "MAINTENANCE")

    def test_summary_normalizes_clinic_status(self):
        patient = {"patient_id": "P-2002"}
        summary = build_summary(patient, [], "  active  ")
        self.assertEqual(summary["clinic_status"], "ACTIVE")

    def test_summary_rejects_missing_patient_id(self):
        with self.assertRaises(ValueError):
            build_summary({"name": "No ID"}, [])

    def test_summary_rejects_non_list_appointments(self):
        with self.assertRaises(ValueError):
            build_summary({"patient_id": "P-3003"}, {"bad": "data"})


if __name__ == "__main__":
    unittest.main()
