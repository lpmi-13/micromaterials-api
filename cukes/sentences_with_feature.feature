@feature
Feature: Get sentences with specific features

	Scenario: We can get sentences for a particular feature

		Given these sentences exist
			| sentence              | features   |
			| Adam's car is lovely. | apostrophe |
			| The cat has a hat     | article    |
		And we want sentences with the 'apostrophe' feature
		When we request sentences
		Then these sentences are returned for the 'apostrophe' feature
			| sentence              |
			| Adam's car is lovely. |


	Scenario: We can limit the number of sentences we receive

		Given these sentences exist
			| sentence                                          | features   |
			| Adam's car is lovely.                             | apostrophe |
			| Adam's passion for artisanal butter is legendary. | apostrophe |
		And we want 1 sentence
		And we want a sentence with the 'apostrophe' feature
		When we request sentences
		Then these sentences are returned for the 'apostrophe' feature
			| sentence              |
			| Adam's car is lovely. |

	Scenario: We can limit sentences by maximum number of words

		Given these sentences exist
			| sentence                                                     | features   |
			| Adam's car is lovely.                                        | apostrophe |
			| Adam's goat cheese pancakes are to die for.                  | apostrophe |
			| The glory of Adam's breakfasts is toast with a bacon coulis. | apostrophe |
		And we want sentences with the 'apostrophe' feature
		And we want sentences with a maximum of 9 words
		When we request sentences
		Then these sentences are returned for the 'apostrophe' feature
			| sentence                                    |
			| Adam's car is lovely.                       |
			| Adam's goat cheese pancakes are to die for. |


	Scenario: No sentences exist

		Given no sentences exist
		And we want sentences with the 'apostrophe' feature
		When we request sentences
		Then no sentences are returned


	Scenario: No sentences have the desired feature

		Given these sentences exist
			| sentence              | features   |
			| Adam's car is lovely. | apostrophe |
		And we want sentences with the 'modal' feature
		When we request sentences
		Then no sentences are returned
