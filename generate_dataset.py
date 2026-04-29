import json
from pathlib import Path

seed = [
    {
        "system": "Você é um assistente de IA com foco em precisão, clareza e segurança.",
        "instruction": "Explique um conceito técnico de forma didática e estruturada.",
        "output": "Comece definindo o conceito, depois apresente um exemplo prático e finalize com limitações e boas práticas."
    },
    {
        "system": "Você é um engenheiro de software sênior.",
        "instruction": "Proponha uma solução eficiente e testável para um problema de dados.",
        "output": "A solução deve incluir modelagem, análise de complexidade, testes unitários e critérios de observabilidade."
    },
    {
        "system": "Você é um pesquisador científico.",
        "instruction": "Avalie criticamente uma hipótese e discuta incertezas.",
        "output": "A avaliação deve separar evidência de inferência, explicitar suposições e sugerir experimentos de validação."
    },
    {
        "system": "Você é um escritor criativo.",
        "instruction": "Crie um texto original com imagens sensoriais e coerência temática.",
        "output": "O texto combina ritmo narrativo, metáforas consistentes e fechamento com impacto emocional."
    },
    {
        "system": "Você é um analista de dados.",
        "instruction": "Interprete resultados estatísticos e destaque riscos de viés.",
        "output": "Interprete métricas com intervalos de confiança, discuta confundidores e recomende próximos passos."
    },
]

entries = []
for i in range(1, 10001):
    base = seed[(i - 1) % len(seed)].copy()
    base["id"] = f"hyp-{i:04d}"
    entries.append(base)

out = Path("hyperon_dataset_10000.json")
out.write_text(json.dumps(entries, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Wrote {len(entries)} entries to {out}")
