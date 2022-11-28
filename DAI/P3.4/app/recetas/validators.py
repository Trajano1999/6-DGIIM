from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re
  
def validate_mayus(valor):
	result = re.match('[A-Z]+.*', valor)
	if result == None:
		raise ValidationError(
			_('%(valor)s debe comenzar por mayúscula'),
			params={'valor': valor}
		)
