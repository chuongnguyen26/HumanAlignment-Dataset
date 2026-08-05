# QualAlign dataset

Human-annotated qualitative coding data used in **QualAlign** (COLM 2026).

Each subdirectory is one research domain. Typical contents:

| File | Description |
|------|-------------|
| `research_questions.txt` | Study research questions / interview directions |
| `train_data_w_gt.csv` | Text chunks with human ground-truth codes |

## Shared columns

Most domains share at least:

| Column | Description |
|--------|-------------|
| `doc_id` | Source document / participant / post identifier |
| `chunk_id` | Unique chunk identifier within the domain |
| `chunk_text` | Text unit to be coded |
| `code_1`, `code_2`, … | Human codes (hierarchical / multi-level; domain-specific) |

Some domains add metadata (e.g. `source`, `source_type`, `timeframe`, `participant_type`, `theme`, `research_question`).

## Domains & research questions

### `adhd_reddit` (154 chunks)
- RQ1: How do adults with ADHD currently use and appropriate existing technologies?
- RQ2: What unmet needs, frustrations, and preferences do adults with ADHD express regarding their current technology use?
- RQ3: What non-technical practices or coping strategies of the adult ADHD community might be supported with technology in the future?

### `data_sharing` (349 chunks)
Interview directions spanning scientists’ data, management plans, libraries, FAIR principles, and repositories.

### `mental_health` (591 chunks)
- RQ1: What master narratives about mental health are emerging across recent interviews, podcasts, and literature?
- RQ2: How are emphases and perspectives within these narratives changing over time?

### `patient_deterioration` (81 chunks)
- RQ1: How do healthcare workers recognise deterioration of ward patients in resource-limited settings?
- RQ2: What organisational, cultural, and decision-making factors influence recognition of deterioration?

### `scrum_quality` (249 chunks)
- RQ1: How do Scrum practitioners define software quality?
- RQ2: How do Scrum values, principles, and prescribed events/activities advance achieving software quality?
- RQ3: Why do some Scrum teams fail to achieve higher software quality?

### `search_systems` (327 chunks)
- RQ1: How do platform/interface limitations shape systematic searching workflows?
- RQ2: How and why do searchers select platforms/databases for evidence synthesis projects?

### `shuffle_music` (784 chunks)
- Why do people download and listen to music?
- Which aspects of the music listening experience are prioritized when people talk about a track on their device?

### `stroke_wearables` (852 chunks)
- RQ1: How do stroke survivors and OTs perceive the usefulness, concerns, and opportunities of wearable arm-use sensors in therapy?
- RQ2: What design considerations and data features would help therapists integrate wearable-derived activity data into rehabilitation planning and follow-up?

## Intended use

- Benchmark automated qualitative coding / schema alignment methods against human annotations.
- Not intended as a substitute for domain-expert qualitative analysis in high-stakes settings without human oversight.

## Provenance & licensing

Domains are derived from publicly available qualitative studies / released materials. When redistributing or publishing derivatives, respect the original study licenses and attribution requirements. Code in this repository is MIT-licensed; the data itself may have additional constraints from source papers.
