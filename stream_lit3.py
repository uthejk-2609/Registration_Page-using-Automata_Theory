
# Import Libraries.
import streamlit as st
import networkx as nx

from streamlit_option_menu import option_menu
from pyformlang.finite_automaton import NondeterministicFiniteAutomaton
from pyformlang.finite_automaton import State, Symbol
from pyformlang.finite_automaton import EpsilonNFA, Epsilon
from pyformlang.pda import PDA, StackSymbol
from pyformlang.regular_expression import Regex

# Definition of the NFA
nfa = NondeterministicFiniteAutomaton()
# Declare Initial State
state0 = State(0)

# Add a start state
nfa.add_start_state(state0)

st.set_page_config(layout = "wide")

with st.sidebar:
  option = option_menu("Stage3", ["Confirm Password"], default_index = 0,
                       icons = ["check"])

if (option == "Confirm Password"):
    st.title("Confirm Password")

    # RE-ENTRY PASSWORD---------------------------------------------------------------------------------------------------------------------------------------------------------
    password = "Nik@2003"
    l = len(password)
    
    re_Password = st.text_input("Enter your Password again: ", key = 13)

    # Declare the states

    # Add a start state
    nfa.add_start_state(State(0))

    # Add a final state
    nfa.add_final_state(State(l))

    # Add the transitions
    for i in range(0, l):
        nfa.add_transition(State(i), Symbol(password[i]), State(i+1))

    # Check if Re-Entered Password is accepted
    flag = nfa.accepts(re_Password)
    if flag:
        st.write("Accepted!")
    else:
        st.write("Rejected!!!")
        
