## Animal is-a object (yes, sort of confusing) Look at the extra credit!
class Animal(object):
	pass

## ??
class Dog(Animal):

	def __init__(self, name):
		## ??
		self.name = name
		
## ??
class Cat(Animal):

	def __init__(self, name):
	## ??
	self.name = name
	
	## Person has-a pet of some kind
	self.pet = None
	
## ??
class Employee(Person):

	def __init__(self, name, salary):
		## ?? Hm?  What is this strange magic?
		super(Employee, self).__init__(name)
		## ??
		self.salary = salary
		
## ??
class Fish(object):
	pass
	
## ??
class Salmon(Fish):
	pass
	
## ??
class Halibut(Fish):
	pass
	
	
## Rover is-a Dog
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ??
mary = person("Mary")

## ??
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()
