import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import networkx as nx
import numpy as np

# List of nodes to add
new_nodes = [
    "Parking Lot A", "Parking Lot A South", "Parking Lot G", "Arboretum Parking","Titan Sports Complex",
    "Arboretum & Botanical Garden", "Children's Center", "Titan Stadium", "Goodwin Field",
    "Anderson Field", "Titan Track & Field", "Titan Softball Field", "Resident Lot 1", 
    "Corporation Yard", "Parking Lot D", "Titan Tennis Courts", "Intramural Field", 
    "East Playfield", "Military Science", "Titan House", "Parking Lot H", 
    "Ruby Gerentology Center", "Parking Lot J", "Resident Hall", "Gastronome", 
    "Housing & Residential Engagement", "University Police", "State College Parking Structure", 
    "Student Recreation Center", "Titan Gymnasium", "Kinesiology & Health Sciences", 
    "Student Health & Counseling Center", "Engineering", "Computer Science", "Golleher Alumni House", 
    "Titan Student Union", "Bookstore/Titan Shop", "Pollack Library", "Education Classroom", 
    "Parking Lot I", "Resident Lot 2", "Auxiliary Services Corporation", "Titan Hall", 
    "Titan Hall Parking Lot", "Visual Arts Center", "Clayes Performing Arts Center", 
    "Humanities", "Parking Lot F", "East Side Parking Structure", "Nutwood Parking Structure", 
    "Greenhouse Complex", "Parking Lot C West", "Parking Lot C East", "McCarthy Hall", 
    "Dan Black Hall", "Modular Complex", "Gordan Hall", "Langsdorf Hall", "Carl's Jr", 
    "Admissions Office", "Steven G. Mihaylo Hall", "Fullerton Marriot", "College Park North Parking Lot", 
    "College Park", "College Park South Parking Lot", "South Parking Lot"
]

# List of edges to add
edges = [
    ("Parking Lot A", "Parking Lot G",                              {'time': 3, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("Parking Lot A", "Parking Lot A South",                        {'time': 3, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("Parking Lot A", "Children's Center",                          {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("Parking Lot A", "Titan Stadium",                              {'time': 2, 'wheelchair_accessible': False,'Passes_Landmark': True}),

    ("Parking Lot A South", "Children's Center",                    {'time': 3, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("Parking Lot A South", "Corporation Yard",                     {'time': 7, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("Parking Lot A South", "Parking Lot D",                        {'time': 4, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("Parking Lot A South", "Titan Track & Field",                  {'time': 7, 'wheelchair_accessible': True, 'Passes_Landmark': True}),
    ("Parking Lot A South", "Titan Sports Complex",                 {'time': 5, 'wheelchair_accessible': True, 'Passes_Landmark': True}),
    ("Parking Lot A South", "Titan Stadium",                        {'time': 5, 'wheelchair_accessible': True, 'Passes_Landmark': True}),
    ("Parking Lot A South", "Corporation Yard",                     {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}),
    ("Parking Lot A South", "Parking Lot D",                        {'time': 2, 'wheelchair_accessible': True, 'Passes_Landmark': True}),


    ("Parking Lot G", "Titan Stadium",                              {'time': 7, 'wheelchair_accessible': True, 'Passes_Landmark': True}),
    ("Parking Lot G", "Goodwin Field",                              {'time': 4, 'wheelchair_accessible': True, 'Passes_Landmark': True}),
    ("Parking Lot G", "Arboretum Parking",                          {'time': 4, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("Parking Lot G", "Titan Sports Complex",                       {'time': 3, 'wheelchair_accessible': True, 'Passes_Landmark': True}),
    ("Parking Lot G", "Anderson Field",                             {'time': 6, 'wheelchair_accessible': True, 'Passes_Landmark': True}),

    ("Arboretum Parking", "Goodwin Field",                          {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}),
    ("Arboretum Parking", "Titan Sports Complex",                   {'time': 5, 'wheelchair_accessible': True, 'Passes_Landmark': True}),
    ("Arboretum Parking", "Anderson Field",                         {'time': 5, 'wheelchair_accessible': True, 'Passes_Landmark': True}),
    ("Arboretum Parking", "Arboretum & Botanical Garden",           {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}),

    ("Titan Sports Complex", "Titan Stadium",                       {'time': 3, 'wheelchair_accessible': True, 'Passes_Landmark': True}),
    ("Titan Sports Complex", "Goodwin Field",                       {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}),
    ("Titan Sports Complex", "Anderson Field",                      {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}),
    ("Titan Sports Complex", "Titan Softball Field",                {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}),
    ("Titan Sports Complex", "Titan Track & Field",                 {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}),
    ("Titan Sports Complex", "East Playfield",                      {'time': 2, 'wheelchair_accessible': True, 'Passes_Landmark': True}),

    ("Children's Center", "Titan Stadium",                          {'time': 2, 'wheelchair_accessible': True, 'Passes_Landmark': True}),

    ("Goodwin Field", "Anderson Field",                             {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}),

    ("Anderson Field", "Titan Softball Field",                      {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}),

    ("Titan Track & Field", "Titan Tennis Courts",                  {'time': 5, 'wheelchair_accessible': True, 'Passes_Landmark': True}),
    ("Titan Track & Field", "Intramural Field",                     {'time': 3, 'wheelchair_accessible': True, 'Passes_Landmark': True}),
    ("Titan Track & Field", "East Playfield",                       {'time': 3, 'wheelchair_accessible': True, 'Passes_Landmark': True}),

    ("Titan Softball Field", "Military Science",                    {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}),
    ("Titan Softball Field", "Titan House",                         {'time': 2, 'wheelchair_accessible': True, 'Passes_Landmark': True}),
    ("Titan Softball Field", "East Playfield",                      {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}),
    
    ("Resident Lot 1", "Gastronome",                                {'time': 3, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("Resident Lot 1", "Housing & Residential Engagement",          {'time': 2, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("Resident Lot 1", "Resident Hall",                             {'time': 2, 'wheelchair_accessible': True, 'Passes_Landmark': False}),

    ("Corporation Yard", "University Police",                       {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("Corporation Yard", "Parking Lot D",                           {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("Corporation Yard", "State College Parking Structure",         {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),

    ("Parking Lot D", "State College Parking Structure",            {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("Parking Lot D", "Student Recreation Center",                  {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("Parking Lot D", "Titan Tennis Courts",                        {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),

    ("Titan Tennis Courts", "Intramural Field",                     {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("Titan Tennis Courts", "Student Recreation Center",            {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("Titan Tennis Courts", "State College Parking Structure",      {'time': 2, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("Titan Tennis Courts", "Titan Gymnasium",                      {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),

    ("Intramural Field", "East Playfield",                          {'time': 0, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("Intramural Field", "Student Recreation Center",               {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("Intramural Field", "Titan Gymnasium",                         {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),

    ("East Playfield", "Military Science",                          {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("East Playfield", "Titan House",                               {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("East Playfield", "Titan Gymnasium",                           {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("East Playfield", "Student Health & Counseling Center",        {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),

    ("Military Science", "Titan House",                             {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("Military Science", "Parking Lot H",                           {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),

    ("Titan House", "Parking Lot H",                                {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("Titan House", "Student Health & Counseling Center",           {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("Titan House", "Ruby Gerentology Center",                      {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("Titan House", "Titan Gymnasium",                              {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),

    ("Parking Lot H", "Student Health & Counseling Center",         {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("Parking Lot H", "Ruby Gerentology Center",                    {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("Parking Lot H", "Parking Lot J",                              {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),

    ("Resident Hall", "Parking Lot J",                              {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("Resident Hall", "Gastronome",                                 {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("Resident Hall", "Housing & Residential Engagement",           {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),

    ("Gastronome", "Parking Lot J",                                 {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("Gastronome", "Student Health & Counseling Center",            {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),

    ("University Police", "Golleher Alumni House",                  {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("University Police", "State College Parking Structure",        {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("University Police", "Titan Student Union",                    {'time': 2, 'wheelchair_accessible': True, 'Passes_Landmark': True}),

    ("State College Parking Structure", "Student Recreation Center",            {'time': 2, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("State College Parking Structure", "Titan Student Union",                  {'time': 2, 'wheelchair_accessible': True, 'Passes_Landmark': True}),
    ("State College Parking Structure", "Golleher Alumni House",                {'time': 2, 'wheelchair_accessible': True, 'Passes_Landmark': True}),

    ("Student Recreation Center", "Titan Student Union",            {'time': 2, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("Student Recreation Center", "Titan Gymnasium",                {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("Student Recreation Center", "Kinesiology & Health Sciences",  {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("Student Recreation Center", "Bookstore/Titan Shop",           {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),

    ("Titan Gymnasium", "Bookstore/Titan Shop",                     {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("Titan Gymnasium", "Kinesiology & Health Sciences",            {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("Titan Gymnasium", "Student Health & Counseling Center",       {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),

    ("Kinesiology & Health Sciences", "Student Health & Counseling Center",     {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}),
    ("Kinesiology & Health Sciences", "Bookstore/Titan Shop",                   {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("Kinesiology & Health Sciences", "Pollack Library",                        {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}),
    ("Kinesiology & Health Sciences", "Engineering",                            {'time': 2, 'wheelchair_accessible': True, 'Passes_Landmark': True}),

    ("Student Health & Counseling Center", "Pollack Library",                   {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}),
    ("Student Health & Counseling Center", "Engineering",                       {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}),
    ("Student Health & Counseling Center", "Ruby Gerentology Center",           {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 

    ("Engineering", "Computer Science",                             {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),    
    ("Engineering", "Parking Lot I",                                {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),    
    ("Engineering", "Education Classroom",                          {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),    

    ("Computer Science", "Parking Lot I",                           {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),    
    ("Computer Science", "Resident Lot 2",                          {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),
    ("Computer Science", "Gastronome",                              {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),    
    
    ("Golleher Alumni House", "Titan Student Union",                {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}),    
    ("Golleher Alumni House", "Auxiliary Services Corporation",     {'time': 2, 'wheelchair_accessible': True, 'Passes_Landmark': False}), 
    ("Golleher Alumni House", "Visual Arts Center",                 {'time': 2, 'wheelchair_accessible': True, 'Passes_Landmark': False}), 

    ("Titan Student Union", "Visual Arts Center",                   {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 
    ("Titan Student Union", "Titan Hall",                           {'time': 2, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 
    ("Titan Student Union", "Bookstore/Titan Shop",                 {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 
    ("Titan Student Union", "Clayes Performing Arts Center",        {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 

    ("Bookstore/Titan Shop", "Clayes Performing Arts Center",       {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 
    ("Bookstore/Titan Shop", "Pollack Library",                     {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 

    ("Pollack Library", "Education Classroom",                      {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 
    ("Pollack Library", "Clayes Performing Arts Center",            {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 
    ("Pollack Library", "Humanities",                               {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 
    ("Pollack Library", "McCarthy Hall",                            {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 
    ("Pollack Library", "Parking Lot I",                            {'time': 2, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 
    ("Pollack Library", "Parking Lot F",                            {'time': 2, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 

    ("Education Classroom", "Parking Lot I",                        {'time': 0, 'wheelchair_accessible': True, 'Passes_Landmark': False}), 
    ("Education Classroom", "Parking Lot F",                        {'time': 0, 'wheelchair_accessible': True, 'Passes_Landmark': False}), 
    ("Education Classroom", "Humanities",                           {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}), 
    ("Education Classroom", "McCarthy Hall",                        {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}), 

    ("Parking Lot I", "Humanities",                                 {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}), 
    ("Parking Lot I", "Parking Lot F",                              {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}), 
    ("Parking Lot I", "Resident Lot 2",                             {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}), 
    ("Parking Lot I", "East Side Parking Structure",                {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}), 

    ("Resident Lot 2", "East Side Parking Structure",               {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}), 
    ("Resident Lot 2", "Resident Lot 1",                            {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}), 

    ("Auxiliary Services Corporation", "Titan Hall",                {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}), 
    ("Auxiliary Services Corporation", "Titan Hall Parking Lot",    {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}), 

    ("Titan Hall", "Titan Hall Parking Lot",                        {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': False}), 

    ("Visual Arts Center", "Titan Hall Parking Lot",                {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 
    ("Visual Arts Center", "Clayes Performing Arts Center",         {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 
    ("Visual Arts Center", "Nutwood Parking Structure",             {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 

    ("Clayes Performing Arts Center", "Nutwood Parking Structure",  {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 
    ("Clayes Performing Arts Center", "Greenhouse Complex",         {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 
    ("Clayes Performing Arts Center", "McCarthy Hall",              {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 
    ("Clayes Performing Arts Center", "Dan Black Hall",             {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 
    ("Clayes Performing Arts Center", "Humanities",                 {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 
    ("Clayes Performing Arts Center", "Gordan Hall",                {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 

    ("Humanities", "Gordan Hall",                                   {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 
    ("Humanities", "Parking Lot F",                                 {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 
    ("Humanities", "McCarthy Hall",                                 {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 

    ("Parking Lot F", "Gordan Hall",                                {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 
    ("Parking Lot F", "Steven G. Mihaylo Hall",                     {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 
    ("Parking Lot F", "Fullerton Marriot",                          {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}),
    ("Parking Lot F", "East Side Parking Structure",                {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 
 
    ("East Side Parking Structure", "Fullerton Marriot",            {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 
    ("East Side Parking Structure", "Steven G. Mihaylo Hall",       {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 

    ("Nutwood Parking Structure", "Parking Lot C West",             {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 
    ("Nutwood Parking Structure", "Parking Lot C East",             {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 

    ("Greenhouse Complex", "McCarthy Hall",                         {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 
    ("Greenhouse Complex", "Dan Black Hall",                        {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 
    ("Greenhouse Complex", "Parking Lot C East",                    {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 

    ("McCarthy Hall", "Parking Lot C East",                              {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 
    ("McCarthy Hall", "Dan Black Hall",                                  {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 
    ("McCarthy Hall", "Gordan Hall",                                     {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 
    ("McCarthy Hall", "Langsdorf Hall",                                  {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 

    ("Dan Black Hall", "Gordan Hall",                               {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 
    ("Dan Black Hall", "Langsdorf Hall",                            {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 
    ("Dan Black Hall", "Modular Complex",                           {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 

    ("Gordan Hall", "Langsdorf Hall",                               {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 
    ("Gordan Hall", "Steven G. Mihaylo Hall",                       {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 

    ("Langsdorf Hall", "Carl's Jr",                                 {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 
    ("Langsdorf Hall", "Steven G. Mihaylo Hall",                    {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}),
    ("Langsdorf Hall", "College Park",                              {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 
    ("Langsdorf Hall", "College Park North Parking Lot",            {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 

    ("Carl's Jr", "Steven G. Mihaylo Hall",                         {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 

    ("Admissions Office", "Steven G. Mihaylo Hall",                 {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 
    ("Admissions Office", "Langsdorf Hall",                         {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 

    ("Steven G. Mihaylo Hall", "Fullerton Marriot",                 {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 
    ("Steven G. Mihaylo Hall", "College Park North Parking Lot",    {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 

    ("College Park North Parking Lot", "College Park",              {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 

    ("College Park", "College Park South Parking Lot",              {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 

    ("College Park South Parking Lot", "South Parking Lot",         {'time': 1, 'wheelchair_accessible': True, 'Passes_Landmark': True}), 
]

# Coordinates of each node
node_coordinates = {
    "Parking Lot A": (200, 240),
    "Parking Lot A South": (200, 450),
    "Parking Lot G": (410, 110),
    "Arboretum Parking": (550, 140),
    "Titan Sports Complex": (480, 360),
    "Arboretum & Botanical Garden": (700, 300),
    "Children's Center": (240, 353),
    "Titan Stadium": (400, 320),
    "Goodwin Field": (510, 250),
    "Anderson Field": (550, 340),
    "Titan Track & Field": (450, 440),
    "Titan Softball Field": (580, 400),
    "Resident Lot 1": (880, 450),
    "Corporation Yard": (180, 500),
    "Parking Lot D": (300, 550),
    "Titan Tennis Courts": (370, 550),
    "Intramural Field": (470, 550),
    "East Playfield": (530, 550),
    "Military Science": (620, 530),
    "Titan House": (620, 560),
    "Parking Lot H": (665, 555),
    "Ruby Gerentology Center": (690, 590),
    "Parking Lot J": (730, 530),
    "Resident Hall": (800, 570),
    "Gastronome": (800, 610),
    "Housing & Residential Engagement": (850, 585),
    "University Police": (168, 630),
    "State College Parking Structure": (230, 630),
    "Student Recreation Center": (290, 630),
    "Titan Gymnasium": (480, 620),
    "Kinesiology & Health Sciences": (450, 690),
    "Student Health & Counseling Center": (620, 650),
    "Engineering": (700, 730),
    "Computer Science": (760, 730),
    "Golleher Alumni House": (168, 700),
    "Titan Student Union": (220, 755),
    "Bookstore/Titan Shop": (370, 750),
    "Pollack Library": (520, 810),
    "Education Classroom": (620, 830),
    "Parking Lot I": (720, 810),
    "Resident Lot 2": (850, 760),
    "Auxiliary Services Corporation": (45, 800),
    "Titan Hall": (95, 870),
    "Titan Hall Parking Lot": (55, 870),
    "Visual Arts Center": (200, 870),
    "Clayes Performing Arts Center": (380, 900),
    "Humanities": (600, 900),
    "Parking Lot F": (730, 900),
    "East Side Parking Structure": (800, 900),
    "Nutwood Parking Structure": (240, 1020),
    "Greenhouse Complex": (370, 980),
    "Parking Lot C West": (200, 1100),
    "Parking Lot C East": (360, 1100),
    "McCarthy Hall": (500, 980),
    "Dan Black Hall": (440, 1030),
    "Modular Complex": (490, 1090),
    "Gordan Hall": (600, 980),
    "Langsdorf Hall": (590, 1040),
    "Carl's Jr": (650, 1000),
    "Admissions Office": (590, 1050),
    "Steven G. Mihaylo Hall": (650, 1080),
    "Fullerton Marriot": (800, 1080),
    "College Park North Parking Lot": (700, 1145),
    "College Park": (670, 1180),
    "College Park South Parking Lot": (670, 1250),
    "South Parking Lot": (670, 1330)
}

# Option 1: BFS for Shortest Path (by number of edges) with Wheelchair Accessibility Check
def bfs_shortest_path(graph, start, end, wheelchair_accessible_required=False):
    from collections import deque

    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current_node, path = queue.popleft()
        
        if current_node == end:
            return path  # Returns path based on number of edges
        
        visited.add(current_node)
        
        for neighbor in graph.neighbors(current_node):
            # Check for wheelchair accessibility if required
            if neighbor not in visited and (not wheelchair_accessible_required or graph[current_node][neighbor].get('wheelchair_accessible', False)):
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)

    return None  # If no path found

# Option 2: DFS with Landmark Condition and Wheelchair Accessibility Check
def dfs_with_landmark(graph, start, end, wheelchair_accessible_required=False):
    def dfs(node, path, visited):
        # Check if destination is reached and the path has an edge with Passes_Landmark=True
        if node == end and any(graph[u][v].get('Passes_Landmark') for u, v in zip(path, path[1:])):
            return path

        visited.add(node)
        for neighbor in graph.neighbors(node):
            # Check for wheelchair accessibility if required
            if neighbor not in visited and (not wheelchair_accessible_required or graph[node][neighbor].get('wheelchair_accessible', False)):
                result = dfs(neighbor, path + [neighbor], visited)
                if result:
                    return result

        visited.remove(node)
        return None

    return dfs(start, [start], set())

# Option 3: Dijkstra’s Algorithm for Minimal Time Path with Wheelchair Accessibility Check
def dijkstra_shortest_path(graph, start, end, wheelchair_accessible_required=False):
    # Filter edges based on wheelchair accessibility if required
    if wheelchair_accessible_required:
        accessible_graph = graph.edge_subgraph((u, v) for u, v, attr in graph.edges(data=True) if attr.get('wheelchair_accessible', False)).copy()
        return nx.shortest_path(accessible_graph, source=start, target=end, weight='time')
    else:
        return nx.shortest_path(graph, source=start, target=end, weight='time')

# Function to plot the graph with only the path from start to end (edges only, no nodes)
def plot_path_edges_only(start_node, end_node, selected_algorithm, wheelchair_access):
    # Load the campus map image
    campus_map = Image.open("CampusMap.jpg").convert("RGB")

    # Resize the image to the desired pixel dimensions
    campus_map_resized = campus_map.resize((1200, 1400))  # Adjust pixel dimensions here as needed
    campus_map_array = np.array(campus_map_resized)

    # Create the graph
    G = nx.Graph()
    G.add_nodes_from(new_nodes)
    G.add_edges_from(edges)

    # Node positions on the map
    node_positions = node_coordinates

    # Compute the shortest path from the start node to the end node (using Dijkstra's algorithm)
    if selected_algorithm == "BFS(Shortest Path by # of edges)":
        path = bfs_shortest_path(G,start_node, end_node, wheelchair_access)
    elif selected_algorithm == "DFS(Path will include a landmark)":
        path = dfs_with_landmark(G,start_node, end_node, wheelchair_access)
    elif selected_algorithm == "Dijkstra's Algorithm(Shortest Path based on time)":
        path = dijkstra_shortest_path(G,start_node,end_node, wheelchair_access)
    else:
        path = nx.shortest_path(G, source=start_node, target=end_node, weight='time')


    # Create the plot
    fig, ax = plt.subplots(figsize=(12, 14))  # Adjust inches if needed for GUI scaling
    ax.imshow(campus_map_array)

    # Draw the edges that are part of the path, without the nodes
    edge_list = list(zip(path[:-1], path[1:]))  # Create edges list from the path
    nx.draw(G, pos=node_positions, ax=ax, with_labels=False, node_size=0, font_size=10,
            font_weight='bold', edge_color='red', node_color='yellow', alpha=0.7,
            edgelist=edge_list)  # Only draw edges in the path, no nodes
    plt.axis('off')  # Turn off axis for map display

    # Remove white space
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)  # This eliminates extra margins

    # Return the figure
    return fig

# Function to display only the campus map without the graph
def display_campus_map():
    fig, ax = plt.subplots(figsize=(12, 14))
    campus_map = Image.open("CampusMap.jpg").convert("RGB")
    campus_map_resized = campus_map.resize((1200, 1400))
    campus_map_array = np.array(campus_map_resized)
    ax.imshow(campus_map_array)
    plt.axis('off')  # Turn off axis for map display
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)  # This eliminates extra margins
    return fig

# Function to handle checkbox toggle event
def on_checkbox_toggle():
    if var.get():  # If checkbox is checked
        print("Checkbox is selected")
    else:  # If checkbox is unchecked
        print("Checkbox is deselected")

# Function to handle algorithm selection
def on_algorithm_select(event):
    selected_algorithm = algorithm_var.get()
    print(f"Selected Algorithm: {selected_algorithm}")

# Function to handle start and end location selection
def on_location_select(event):
    start_location = start_var.get()
    end_location = end_var.get()
    print(f"Start Location: {start_location}")
    print(f"End Location: {end_location}")

# Function to toggle the map between campus map and graph with nodes/edges
def toggle_graph():
    global canvas  # Make sure to refer to the global canvas
    
    # Destroy the old canvas if it exists
    if canvas.get_tk_widget():
        canvas.get_tk_widget().destroy()

    # Get selected start and end nodes
    start_node = start_var.get()
    end_node = end_var.get()
    selected_algorithm = algorithm_var.get()
    wheelchair_access = var.get()

    # Plot either the graph (edges only) or the campus map depending on the checkbox status
    if graph_var.get():
        fig = plot_path_edges_only(start_node, end_node, selected_algorithm, wheelchair_access)  # Only show the path (edges)
    else:
        fig = display_campus_map()

    # Create a new canvas for the updated figure
    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)  # A tkinter widget to embed the plot
    canvas.draw()

    # Pack the new canvas widget into the window
    canvas.get_tk_widget().pack()

# Initialize the main window
root = tk.Tk()
root.title("Campus Navigation System")

# Create a frame to hold widgets on the left side
left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, padx=10, pady=10)

# Create the dropdown for algorithm selection
algorithm_label = tk.Label(left_frame, text="Select Algorithm:")
algorithm_label.grid(row=0, column=0, sticky="w")

algorithm_var = tk.StringVar()
algorithm_dropdown = ttk.Combobox(left_frame, textvariable=algorithm_var, values=["BFS(Shortest Path by # of edges)", "DFS(Path will include a landmark)", "Dijkstra's Algorithm(Shortest Path based on time)"])
algorithm_dropdown.grid(row=0, column=1)

algorithm_dropdown.bind("<<ComboboxSelected>>", on_algorithm_select)

# Create the checkbox for wheelchair accessibility
var = tk.BooleanVar()
checkbox = tk.Checkbutton(left_frame, text="Wheelchair Accessible", variable=var, command=on_checkbox_toggle)
checkbox.grid(row=1, columnspan=2, pady=5)

# Create the Start Position and End Position dropdowns in the same row
location_label = tk.Label(left_frame, text="Select Start and End Locations:")
location_label.grid(row=2, columnspan=2, pady=5)

# Start location dropdown
start_var = tk.StringVar()
start_label = tk.Label(left_frame, text="Start Position:")
start_label.grid(row=3, column=0, sticky="w")
start_location_dropdown = ttk.Combobox(left_frame, textvariable=start_var, values=new_nodes)
start_location_dropdown.grid(row=3, column=1)

# End location dropdown
end_var = tk.StringVar()
end_label = tk.Label(left_frame, text="End Position:")
end_label.grid(row=4, column=0, sticky="w")
end_location_dropdown = ttk.Combobox(left_frame, textvariable=end_var, values=new_nodes)
end_location_dropdown.grid(row=4, column=1)

# Bind the location selection to handle changes
start_location_dropdown.bind("<<ComboboxSelected>>", on_location_select)
end_location_dropdown.bind("<<ComboboxSelected>>", on_location_select)

# Create a Checkbutton to toggle the display of the graph and campus map
graph_var = tk.BooleanVar()
graph_button = tk.Checkbutton(left_frame, text="Show Graph", variable=graph_var, command=toggle_graph)
graph_button.grid(row=5, columnspan=2, pady=10)

# Create a canvas for matplotlib plot
canvas_frame = tk.Frame(root)
canvas_frame.pack(side=tk.RIGHT, padx=10, pady=10)

# Initially display the campus map (without the graph)
fig = display_campus_map()

# Create the canvas to display the matplotlib figure inside the tkinter window
canvas = FigureCanvasTkAgg(fig, master=canvas_frame)  # A tkinter widget to embed the plot
canvas.draw()

# Pack the canvas widget into the window
canvas.get_tk_widget().pack()

# Run the application
root.mainloop()