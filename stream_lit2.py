
# Import Libraries.
import streamlit as st
import networkx as nx

from streamlit_option_menu import option_menu
from pyformlang.finite_automaton import NondeterministicFiniteAutomaton
from pyformlang.finite_automaton import State, Symbol
from pyformlang.finite_automaton import EpsilonNFA, Epsilon
from pyformlang.pda import PDA, StackSymbol
from pyformlang.regular_expression import Regex

# Definition of Epsilon i.e; Lambda
epsilon = Epsilon()

# Definition of the NFA
nfa = NondeterministicFiniteAutomaton()

# Declare Initial State
state0 = State(0)

# Add a start state
nfa.add_start_state(state0)

st.set_page_config(layout = "wide")

with st.sidebar:
  option = option_menu("Stage2", ["Phone Number", "Password"], default_index = 0,
                       icons = ["phone", "asterisk"])
  
if (option == "Password"):
  st.title("Password")

  # PASSWORD----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Password = st.text_input("Enter your Paasword: ", key = 14)

  # Declare the states
  state38 = State(38)
  state39 = State(39)
  state40 = State(40)
  state41 = State(41)
  state42 = State(42)

  # Add a final state
  nfa.add_final_state(state42)

  # Add the transitions
  for i in range(0, 9 + 1):  
      nfa.add_transition(state0, str(i), state38)
      nfa.add_transition(state38, str(i), state39)
      nfa.add_transition(state39, str(i), state40)
      nfa.add_transition(state40, str(i), state41)
      nfa.add_transition(state41, str(i), state42)

      nfa.add_transition(state0, str(i), state0)
      nfa.add_transition(state38, str(i), state38)
      nfa.add_transition(state39, str(i), state39)
      nfa.add_transition(state40, str(i), state40)
      nfa.add_transition(state41, str(i), state41)
      nfa.add_transition(state42, str(i), state42)


  for i in range(ord('A'), ord('Z') + 1):
      nfa.add_transition(state0, chr(i), state38)
      nfa.add_transition(state38, chr(i), state39)
      nfa.add_transition(state39, chr(i), state40)
      nfa.add_transition(state40, chr(i), state41)
      nfa.add_transition(state41, chr(i), state42)

      nfa.add_transition(state0, chr(i), state0)
      nfa.add_transition(state38, chr(i), state38)
      nfa.add_transition(state39, chr(i), state39)
      nfa.add_transition(state40, chr(i), state40)
      nfa.add_transition(state41, chr(i), state41)
      nfa.add_transition(state42, chr(i), state42)

  for i in range(ord('a'), ord('z') + 1):
      nfa.add_transition(state0, chr(i), state38)
      nfa.add_transition(state38, chr(i), state39)
      nfa.add_transition(state39, chr(i), state40)
      nfa.add_transition(state40, chr(i), state41)
      nfa.add_transition(state41, chr(i), state42)

      nfa.add_transition(state0, chr(i), state0)
      nfa.add_transition(state38, chr(i), state38)
      nfa.add_transition(state39, chr(i), state39)
      nfa.add_transition(state40, chr(i), state40)
      nfa.add_transition(state41, chr(i), state41)
      nfa.add_transition(state42, chr(i), state42)

  for i in ('_', '@', '!', '$', '-', '&', '*', '#'):
      nfa.add_transition(state0, i, state38)
      nfa.add_transition(state38, i, state39)
      nfa.add_transition(state39, i, state40)
      nfa.add_transition(state40, i, state41)
      nfa.add_transition(state41, i, state42)

      nfa.add_transition(state0, i, state0)
      nfa.add_transition(state38, i, state38)
      nfa.add_transition(state39, i, state39)
      nfa.add_transition(state40, i, state40)
      nfa.add_transition(state41, i, state41)
      nfa.add_transition(state42, i, state42)

  # Check if Password is accepted  
  flag14 = nfa.accepts(Password)
  if flag14:
    st.write("Accepted!")
  else:
    st.write("Rejected!!!")

  def check(password, spl, num):
    result = []
    
    for i in spl:
        if i in password:
            result.append("Yes")
        else:
            result.append("No")
    for i in num:
        if str(i) in password:
            result.append("Okay")
        else:
            result.append("No")
    return result

  spl = ['_', '@', '!', '$', '-', '&', '*', '#']
  num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  result = check(Password, spl, num)

  if ('Yes' in result) and ('Okay' in result):
      st.write(" Very Strong Password")
  elif 'Yes' in result: 
      st.write("Strong Password")
  elif 'Okay' in result:
      st.write("Strong Password") 
  else:
      st.write("Weak Password")

if (option == "Phone Number"):
  st.title("Phone Number")

  # PHONE NUMBER------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  # Phn_Code = st.text_input("Enter your Country Code: ", key = 16)
  Phn_Code = st.selectbox("Select your Mobile Country Code", ["91", "1", "1340", "1670", "1767", "1664", "1721"])

  # st.write("91 | 1 | 1340 | 1670 | 1767 | 1664 | 1721")
  regex5 = Regex("91 | 1 | 1664 | 1721")

  #Check if the country code is accepted
  flag16 = regex5.accepts([Phn_Code])
  if flag16:
    st.write("Accepted!")
  else:
    st.write("Sorry for the Inconvience, Services aren't available. Coming SOON :(")

  Phn_No = st.text_input("Enter your Mobile Number: ", key = 12)

  # Declare the states
  state28 = State(28)
  state29 = State(29)
  state30 = State(30)
  state31 = State(31)
  state32 = State(32)
  state33 = State(33)
  state34 = State(34)
  state35 = State(35)
  state36 = State(36)
  state37 = State(37)

  # Add a final state
  nfa.add_final_state(state37)

  # Add the transitions
  for i in range(0, 9 + 1):
      nfa.add_transition(state0, str(i), state28)
      nfa.add_transition(state28, str(i), state29)
      nfa.add_transition(state29, str(i), state30)
      nfa.add_transition(state30, str(i), state31)
      nfa.add_transition(state31, str(i), state32)
      nfa.add_transition(state32, str(i), state33)
      nfa.add_transition(state33, str(i), state34)
      nfa.add_transition(state34, str(i), state35)
      nfa.add_transition(state35, str(i), state36)
      nfa.add_transition(state36, str(i), state37)

  #Check if a Phone_Number is accepted
  flag12 = nfa.accepts(Phn_No)
  if flag12:
    st.write("Accepted!")
  else:
    st.write("Rejected!!!")

  # Recovery Phone Number---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  # Check if Recovery Phone Number is accepted
  recov_phn = st.text_input("Enter your Recovery Phone Number: ", key = 13)

  st.write("Dear User, please enter a alter Mobile Number.")
  flag13 = nfa.accepts(recov_phn)
  if recov_phn != Phn_No:
      if len(recov_phn) == 10:
          flag13 = nfa.accepts(recov_phn)
          st.write("Accepted!")
      else:
          st.write("Rejected!!!")
  else:
      st.write("Rejected!!!")


