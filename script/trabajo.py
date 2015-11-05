#!/usr/bin/python
# -*- coding: utf-8 -*-

s = True
n = False

print("Conteste s (sí) o n (no) a mis preguntas.")
a = input('¿Te sientes listo para comenzar el día?: ')
if a == s:
	b = input('¿Te cepillaste?: ')
	if b == s:
		c = input('¿Te vestiste?: ' )
		if c == s:
			d = input('¿Arreglaste la cama?: ')
			if d == s:
				print '¡Muy bien! Ve al trabajo.'
else:
	a == "n"
	print 'Bueno, sigue durmiendo campeón!'