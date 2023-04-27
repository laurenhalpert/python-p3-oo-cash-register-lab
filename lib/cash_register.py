#!/usr/bin/env python3
import ipdb
class CashRegister:
  
  def __init__(self, discount = 0):
    
    self.discount = discount
    self.total = 0
    self.items =[]
    self.last_transaction = 0
  def add_item(self, title, price, quantity=1):
    self.last_transaction = price * quantity
    self.total += (price* quantity)
    for i in range(quantity):
      self.items.append(title)
  def apply_discount(self):
    if self.discount >0:
      self.total = int(self.total*((100-self.discount)/100))
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print(f"There is no discount to apply.")
  def void_last_transaction(self):
    self.total -= self.last_transaction
  