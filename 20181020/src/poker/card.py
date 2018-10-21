# -*- coding: utf-8 -*-

class Card(object):
  def __init__(self, card):
    if self.__validate__(card):
      raise ValueError
    self.value = card[0]
    self.suit = card[1]

  def __repr__(self):
    return '<Card: {{ value: {}, suit: {} }}>'.format(self.value, self.suit)
    
  def __validate__(self, raw_card):
    error = True
    if len(raw_card) == 2:
      if (raw_card[0] in {'2','3','4','5','6','7','8','9','T','J','Q','K','A'}) and (raw_card[1] in {'C','D','H','S'}):
        error = False
    return error