@word
Feature: Get sentences with words

	Scenario: We can get sentences containing a specific word

		Given these sentences exist
			| sentence                                      | features   |
			| Rich has a deep love for custard doughnuts.   | plural     |
			| The plums are so sweet and so cold.           | plural     |
			| The love of Rich's life is the scent of jade. | apostrophe |
		And we want sentences containing the word 'love'
		When we request sentences
		Then these sentences are returned
			| sentence                                      |
			| Rich has a deep love for custard doughnuts.   |
			| The love of Rich's life is the scent of jade. |

	Scenario: We can get sentences containing a specific word and POS, negative case

		Given these sentences exist
			| sentence         | features       | pos                                                   |
			| I Love.          | simple_present | personal_pronoun,first_person_simple_present          |
			| I Love The Cake. | singular_noun  | PRP,first_person_simple_present,article,singular_noun |
		And we want sentences with the word 'Love' as a 'singular_noun'
		When we request sentences
		Then no sentences are returned

	Scenario: We can get sentences containing a specific word and POS

		Given these sentences exist
			| sentence    | features       | pos                                          |
			| I Love.     | simple_present | personal_pronoun,first_person_simple_present |
			| Love hurts. | singular_noun  | singular_noun,first_person_simple_present    |
		And we want sentences with the word 'Love' as a 'singular_noun'
		When we request sentences
		Then these sentences are returned
			| sentence    |
			| Love hurts. |


	Scenario: No sentences exist

		Given no sentences exist
		And we want sentences containing the word 'love'
		When we request sentences
		Then no sentences are returned


	Scenario: No sentences contain the desired word

		Given these sentences exist
			| sentence              | features   |
			| Adam's car is lovely. | apostrophe |
		And we want sentences with the 'modal' feature
		When we request sentences
		Then no sentences are returned
