Feature: We are testing Hamming class - It should return the Hamming distance between two strands

  @hamming
  Scenario: We have two identical short strands
    Given two strands
    """
    AAA,AAA
    """
    When they are the same
    Then output should be 0


  @hamming
  Scenario: We have two different short strands
    Given two strands
    """
    ATGT,GATA
    """
    When they are different
    Then output should be 4


  @hamming
  Scenario: We have two identical long strands
    Given two strands
    """
    GGACTGAAATCTG,GGACTGAAATCTG
    """
    When they are the same
    Then output should be 0


  @hamming
  Scenario: We have two different long strands
    Given two strands
    """
    GGACGGATTCTG,AGGACGGATTCT
    """
    When they are different
    Then output should be 9


  @hamming
  Scenario: First strand is longer than second
    Given two strands
    """
    ATTG,ATG
    """
    When they are not same length
    Then output should be "Strands should be the same length"


  @hamming
  Scenario: Second strand is longer than first
    Given two strands
    """
    GTA,GTAG
    """
    When they are not same length
    Then output should be "Strands should be the same length"


  @hamming
  Scenario: Wrong type of first strand
    Given two strands
    """
    123,GGT
    """
    When type of first is not str
    Then output should be "Wrong type of strands"


  @hamming
  Scenario: Wrong type of second strand
    Given two strands
    """
    ATG,942
    """
    When type of second is not str
    Then output should be "Wrong type of strands"