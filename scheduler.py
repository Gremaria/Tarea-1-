from typing import List, Dict

def compatibilidad(recurso: Dict, trabajo: Dict) -> bool:
    return trabajo["category"] in recurso["categories"]


def tiempos_cronograma(recursos: List[Dict], trabajos: List[Dict]) -> dict:

    trabajos = sorted(trabajos, key=lambda x: x["span"], reverse=True)

    contadores = {r["id"]: 0 for r in recursos}
    total = {"lista": [], "tiempo_ms": 0, "uso_recursos": contadores}

    for trabajo in trabajos:
        mejor_recurso = None
        menor_tiempo = float("inf")

        for recurso in recursos:
            if compatibilidad(recurso, trabajo):
                if contadores[recurso["id"]] < menor_tiempo:
                    menor_tiempo = contadores[recurso["id"]]
                    mejor_recurso = recurso

        if mejor_recurso:
            rid = mejor_recurso["id"]

            inicio = contadores[rid]
            fin = inicio + trabajo["span"]

            total["lista"].append({
                "id": trabajo["id"],
                "recurso": rid,
                "inicio": inicio,
                "fin": fin,
                "retraso": max(0, fin - trabajo["deadline"]),
                "cumple": fin <= trabajo["deadline"]
            })

            contadores[rid] = fin

    return total