# shared-contracts usage

Use as git dependency or package publish target.

Example (requirements.txt):

```txt
git+ssh://<git-host>/<org>/shared-contracts.git@main#egg=stagelog-shared-contracts
```

Then import:

```python
from contracts.notification_events import to_detail_type
from contracts.internal_api_contracts import EVENTS_INTERNAL_BATCH_SUMMARY
from stagelog_shared.django_utils import common_response, login_check
from stagelog_shared.internal_api import get_users_batch
```
