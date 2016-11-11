Feature: Give me some sentences

	We want sentences from the API.

	Scenario: We can request sentences for a particular feature

		Given these sentences exist
			| sentence              | features   |
			| Adam's car is lovely. | apostrophe |
		When we request sentences with the 'apostrophe' feature
		Then these sentences are returned
			| sentence              |
			| Adam's car is lovely. |


	Scenario: We can limit the number of sentences we receive

		Given these sentences exist
			| sentence                                          | features   |
			| Adam's car is lovely.                             | apostrophe |
			| Adam's passion for artisanal butter is legendary. | apostrophe |
		When we request one sentence with the 'apostrophe' feature
		Then these sentences are returned
			| sentence              |
			| Adam's car is lovely. |
