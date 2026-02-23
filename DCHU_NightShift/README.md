#Project File Tree

DCHU_NightShift/
|
├─ services/
| ├─ QCFD_service/
| | ├─ run.py
| | |
| | ├─ domain/
| | │ ├─ base_class.py
| | │ ├─ interface.py
| | | |
| | │ ├─ src/
| | │ | ├─ extract/
| | │ | ├─ transform/
| | │ | ├─ load/
| | │ | ├─ validation/
| | │ | └─ orchestration/
| | | |
| | │ └─ infrastructure/
| | |
| | ├─ config/
| | └─ Dockerfile
| |
| └─another_service/...
|
├─ data/
|
├─ docker-compose.yml
├─ README.md
|
├─ gateway/
└─ tests/
