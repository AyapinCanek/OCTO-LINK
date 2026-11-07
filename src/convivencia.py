"""Toy consent-policy simulator for OCTO-LINK. No psychological inference."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Situation:
    """Synthetic interaction; all signals are explicit, not inferred."""
    help_requested: bool
    consent_to_approach: bool | None
    request_withdrawn: bool = False


@dataclass(frozen=True)
class Decision:
    action: str
    explanation: str


def choose_action(situation: Situation) -> Decision:
    """Conservative rule-based baseline; never executes physical movements."""
    if situation.request_withdrawn:
        return Decision("detenerse", "La persona retiró su solicitud o permiso.")
    if not situation.help_requested:
        return Decision("no_intervenir", "No hay una solicitud explícita de ayuda.")
    if situation.consent_to_approach is False:
        return Decision("respetar_distancia", "No se autorizó acercamiento.")
    if situation.consent_to_approach is None:
        return Decision("pedir_permiso", "Hay una solicitud, pero no consta permiso para acercarse.")
    return Decision("ofrecer_ayuda", "Hay solicitud y permiso explícitos; ofrecer asistencia sin imponerla.")


def run() -> None:
    cases = {
        "ayuda_con_permiso": Situation(True, True),
        "ayuda_sin_permiso_de_acercarse": Situation(True, False),
        "permiso_desconocido": Situation(True, None),
        "sin_solicitud": Situation(False, True),
        "solicitud_retirada": Situation(True, True, True),
    }
    for name, case in cases.items():
        decision = choose_action(case)
        print(f"{name}: {decision.action} — {decision.explanation}")


if __name__ == "__main__":
    run()
