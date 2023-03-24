
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

st.set_page_config(layout="wide")

with st.sidebar:
  option = option_menu("Stage1", ["Basic Details", "Education and Occupation", "Address"], default_index = 0,
                       icons = ["list-task", "pencil", "house"])

if (option == "Basic Details"):
  st.title("Basic Details")
  
  left2, right2 = st.columns(2)
  with left2:
    # Declare Initial State
    state0 = State(0)
    # Add a start state
    nfa.add_start_state(state0)

    # NAME--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    First_Name = st.text_input("Enter your First Name: ", key = 1)

    # Declare the states
    state1 = State(1)
    # state2 = State(2)

    # Declare the symbols
    symb_space = Symbol(" ")

    # Add a final state
    nfa.add_final_state(state1)

    # Add the transitions
    for i in range(ord('A'), ord('Z') + 1):
      nfa.add_transition(state0, chr(i), state1)

      nfa.add_transition(state1, chr(i), state1)
#      nfa.add_transition(state2, chr(i), state3)

#    nfa.add_transition(state1,symb_space, state2)

    for i in range(ord('a'), ord('z') + 1):
      nfa.add_transition(state1, chr(i), state1)

    # Check if Name is accepted
    flag1 = nfa.accepts(First_Name)
    if flag1:
      st.write("Accepted!")
    else:
      st.write("Rejected!!!")
  
  with right2:
    Last_Name = st.text_input("Enter your Last Name: ", key = 12)
    
    # Declare the states
    state3 = State(3)

    # Add a final state
    nfa.add_final_state(state3)

    # Add the transitions
    for i in range(ord('A'), ord('Z') + 1):
      nfa.add_transition(state0, chr(i), state3)

      nfa.add_transition(state3, chr(i), state3)

    for i in range(ord('a'), ord('z') + 1):
      nfa.add_transition(state3, chr(i), state3)

    flag12 = nfa.accepts(Last_Name)
    if flag12:
      st.write("Accepted!")
    else:
      st.write("Rejected!!!")
    
  #AGE----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  # Age = st.text_input("Enter your Age: ", key = 2)
  Age = st.select_slider('Select your age', 
                          options=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199],
                          )
  
  # Declare the states
  state4 = State(4)
  state5 = State(5)
  state6 = State(6)
  state7 = State(7)
  
  # Add a final state
  nfa.add_final_state(state5)
  nfa.add_final_state(state7)
  
  # Add the transitions
  nfa.add_transition(state0, Symbol("1"), state6)
  
  for i in range(8, 9 + 1):
      nfa.add_transition(state6, str(i), state7)
  
  for i in range(2, 9 + 1):  
      nfa.add_transition(state0, str(i), state4)
  
  for i in range(0, 9 + 1):  
      nfa.add_transition(state4, str(i), state5)
  
  #Check if Age is accepted
  flag2 = nfa.accepts(str(Age))
  if flag2:
    st.write("Accepted!")
  else:
    st.write("Rejected!!!")
  
  # DOB--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  DOB = st.text_input("Enter your Date Of Birth: (DD/MM/YYYY) ", key = 3)
  
  # Declare the states
  state8 = State(8)
  state9 = State(9)
  state10 = State(10)
  state11 = State(11)
  state12 = State(12)
  state13 = State(13)
  state14 = State(14)
  state15 = State(15)
  state16 = State(16)
  state17 = State(17)
  
  # Declare the symbols
  symb_Hyphen = Symbol("-")
  symb_Slash = Symbol("/")
  
  # Add a final state
  nfa.add_final_state(state17)
  
  # Add the transitions  
  nfa.add_transition(state9, symb_Hyphen, state10)
  nfa.add_transition(state12, symb_Hyphen, state13)
  
  nfa.add_transition(state9, symb_Slash, state10)
  nfa.add_transition(state12, symb_Slash, state13)
  
  for i in range(0, 3 + 1):
      nfa.add_transition(state0, str(i), state8)
  
  for i in range(0, 1 + 1):
      nfa.add_transition(state10, str(i), state11)
  
  for i in range(1, 2 + 1):
      nfa.add_transition(state13, str(i), state14)
  
  for i in range(0, 9 + 1):
      nfa.add_transition(state8, str(i), state9)
      nfa.add_transition(state11, str(i), state12)
      nfa.add_transition(state14, str(i), state15)
      nfa.add_transition(state15, str(i), state16)
      nfa.add_transition(state16, str(i), state17)
  
  #Check if DOB is accepted
  flag3 = nfa.accepts(DOB)
  if flag3:
    st.write("Accepted!")
  else:
    st.write("Rejected!!!")
  
  # GENDER------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  st.write("M -> Male")
  st.write("F -> Female")
  st.write("N -> Other")
  
  # Gender = st.text_input("Enter your Gender: ", key = 4)
  Gender = st.radio("Select your Gender", ["M", "F", "N"])
  
  # Declare the states
  state18 = State(18)
  state19 = State(19)
  state20 = State(20)
  
  # Declare the symbols
  symb_M = Symbol("M")
  symb_F = Symbol("F")
  symb_NA = Symbol("N")
  
  # Add a final state
  nfa.add_final_state(state18)
  nfa.add_final_state(state19)
  nfa.add_final_state(state20)
  
  # Add the transitions  
  nfa.add_transition(state0, symb_M, state18)
  nfa.add_transition(state0, symb_F, state19)
  nfa.add_transition(state0, symb_NA, state20)
  
  nfa.add_transition(state0, Symbol("Male"), state18)
  nfa.add_transition(state0, Symbol("Female"), state19)
  nfa.add_transition(state0, Symbol("Other"), state20)
  
  #Check if Gender is accepted
  flag4 = nfa.accepts(Gender)
  if flag4:
    st.write("Accepted!")
  else:
    st.write("Rejected!!!")

if (option == "Education and Occupation"):
  st.title("Profession and Qualification")

  # Declare Initial State
  state0 = State(0)
  # Add a start state
  nfa.add_start_state(state0)

  # EMAIL-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  EMail = st.text_input("Enter your E-Mail: ", key = 5)

  # Declare the states
  state21 = State(21)

  # Declare the symbols
  symb_Dot = Symbol(".")
  symb_UnderScore = Symbol("_")
  # x = ["@gmail.com", "@icloud.com"]

  # Add a final state
  nfa.add_final_state(state21)

  # Add the transitions
  for i in range(ord('a'), ord('z') + 1):
    nfa.add_transition(state0, chr(i), state0)
    nfa.add_transition(state21, chr(i), state21)

  for i in range(ord('A'), ord('Z') + 1):
    nfa.add_transition(state0, chr(i), state0)
    nfa.add_transition(state21, chr(i), state21)

  nfa.add_transition(state0, symb_Dot, state0)  
  nfa.add_transition(state21, symb_Dot, state21)
  nfa.add_transition(state0, symb_UnderScore, state0)
  nfa.add_transition(state21, symb_UnderScore, state21)
  nfa.add_transition(state0, Symbol("@"), state21)

  for i in range(0, 9 + 1):
      nfa.add_transition(state0, str(i), state0)
      nfa.add_transition(state21, str(i), state21)

  # Check if a EMail is accepted
  flag5 = nfa.accepts(EMail)
  if flag5:
    st.write("Accepted!")
  else:
    st.write("Rejected!!!")

  # Qualification_Profession------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Qualification = st.text_input("Enter your Qualification", key = 10)

  st.write("BTech | MTech | BCom | PhD | BSE | 10th | Intermediate | M.Sc | B.Ed | CA | MBBS | Other")
  regex3 = Regex("BTech | MTech | BCom | PhD | BSE | 10th | Intermediate | M.Sc | B.Ed | CA | MBBS | Other")

  flag10 = regex3.accepts([Qualification])
  if flag10:
    st.write("Accepted!")
  else:
    st.write("Rejected!!!")

  Profession= st.text_input("Enter your Profession", key = 11)

  st.write("Student | Teacher | Business | Farmer | Doctor | Entrepreneur | Police | Cuisinier | Other")
  regex4 = Regex("Student | Teacher | Business | Farmer | Doctor | Entrepreneur | Police | Cuisinier | Other")

  flag11 = regex4.accepts([Profession])
  if flag11:
    st.write("Accepted!")
  else:
    st.write("Rejected!!!")

if (option == "Address"):
  st.title("Locality Address")

  # Declare Initial State
  state0 = State(0)
  # Add a start state
  nfa.add_start_state(state0)

  # ADDRESS-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  left1, right1 = st.columns(2)
  with left1:
  # Country
  # Country = st.text_input("Enter your Country: ", key = 6)
    regex1 = Regex("India | SriLanka_Provisions | Pakistan_Provisions | Afganisthan_Provisions")
    Country = st.selectbox("Select your Country", ["India", "SriLanka_Provisions",  "Pakistan_Provisions",  "China", "Bangladesh", "Nepal", "Germany", "United_Kingdom","Brazil","Argentina", "Afganisthan_Provisions"])
    UnCountry = ["China", "Bangladesh", "Nepal", "Germany", "United_Kingdom", "Brazil", "Argentina"]
    
    # Check of a Country is accepted
    flag6 = regex1.accepts([Country])
    if flag6:
      st.write("Accepted!")
    else:
      st.write("Sorry for the Inconvience, Services aren't available. Coming SOON :(")

  with right1:
    # States
    # States = st.text_input("Enter your State: ", key = 7)
    # States = st.radio("Check Box your State", ["Andhra_Pradesh", "Telangana", "Tamil_Nadu", "Karnataka", "Kerala", "Gujarat", "Madhya_Pradesh", "Maharashtra", "Delhi", "Rajasthan", "Punjab"])
    if Country == "India":
      States = st.selectbox("Select your State",  ['Andhra_Pradesh', 'Arunachal_Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana', 'Himachal_Pradesh', 'Jammu_Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya_Pradesh', 'Maharashtra', 'Manipur','Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttarakhand', 'Uttar_Pradesh',' West_Bengal'])
      regex2 = Regex("Andhra_Pradesh |Arunachal_Pradesh | Assam | Bihar | Chhattisgarh | Gujarat | Haryana | Jharkhand | Karnataka |Kerala | Madhya_Pradesh | Maharashtra | Manipur | Nagaland | Odisha | Punjab | Rajasthan | Tamil_Nadu | Telangana | Tripura | Uttarakhand | Uttar_Pradesh | West_Bengal")
    elif Country == "SriLanka_Provisions":
      States = st.selectbox("Select your State", ['Central_Province', 'Eastern_Province', 'North_Central_Province', 'Northern_Province', 'North_Western_Province', 'Sabaragamuwa_Province', 'Southern_Province', 'Uva_Province', 'Western_Province'])
      regex2 = Regex('Central_Province | Eastern_Province | North_Western_Province | Sabaragamuwa_Province | Southern_Province | Western_Province')
    elif Country == "Pakistan_Provisions":
      States = st.selectbox("Select your State", ['Balochistan', 'Gilgit_Baltistan', 'Khyber_Pakhtunkhwa', 'Punjab', 'Sindh'])
      regex2 = Regex('Balochistan | Punjab | Sindh')
    elif Country == "Afganisthan_Provisions":
      States = st.selectbox("Select your State", ['Badakhshan','Balkh','Baghlan','Kunar','Nangarhar','Herat','Jowzjan','Kandahar','Kapisa','Laghman','Logar','Nimruz','Paktia', 'Parwan', 'Samangan','Sare Pol', 'Takhar', 'Urozgan', 'Zabul'])
      regex2 = Regex('Badakhshan | Baghlan | Kunar | Nangarhar | Herat | Jowzjan | Kandahar | Nimruz | Paktia | Parwan | Samangan | Urozgan | Zabul')
    elif Country in UnCountry:
      States = ""
      regex2 = Regex("")
      
    # Check if a locality State is accepted
    flag7 = regex2.accepts([States])
    if flag7:
      st.write("Accepted!")
    else:
      st.write("Sorry for the Inconvience, Services aren't available. Coming SOON :(")

  # PINCODE
  PINCODE = st.text_input("Enter your locality Pincode: ", key = 8)

  # Delcare the states
  state22 = State(22)
  state23 = State(23)
  state24 = State(24)
  state25 = State(25)
  state26 = State(26)
  state27 = State(27)

  # Add a final state
  nfa.add_final_state(state27)

  # Add the transitions
  for i in range(0, 9 + 1):
      nfa.add_transition(state0, str(i), state22)
      nfa.add_transition(state22, str(i), state23)
      nfa.add_transition(state23, str(i), state24)
      nfa.add_transition(state24, str(i), state25)
      nfa.add_transition(state25, str(i), state26)
      nfa.add_transition(state26, str(i), state27)

  # Check if a PINCODE is accepted
  flag8 = nfa.accepts(PINCODE)
  if flag8:
    st.write("Accepted!")
  else:
    st.write("Rejected!!!")

  # Area----------------------------------------------------------------------------------------------
  Address = st.text_input("Enter your Address: ", key = 9)

  # Delcare the states
  state_B = State("B")
  state_C = State("C")

  # Add a final state
  nfa.add_final_state(state_C)

  # Add the transitions
  nfa.add_transition(state0, Symbol("-"), state0)
  nfa.add_transition(state0, Symbol("/"), state0)

  for i in (','):
      nfa.add_transition(state0, i, state_B)
      nfa.add_transition(state_B, i, state_C)

  for i in (' '):
      nfa.add_transition(state_B, i, state_B)
      nfa.add_transition(state_C, i, state_C)

  for i in range(0, 9 + 1):
      nfa.add_transition(state0, str(i), state0)

  for i in range(ord('A'), ord('Z') + 1):
      nfa.add_transition(state_B, chr(i), state_B)
      nfa.add_transition(state_C, chr(i), state_C)    

  for i in range(ord('a'), ord('z') + 1):
      nfa.add_transition(state_B, chr(i), state_B)
      nfa.add_transition(state_C, chr(i), state_C)    

  # Check if a Address is accepted
  st.write("Address Schema-> Door Num, Street Name, City Name")
  flag9 = nfa.accepts(Address)
  if flag9:
    st.write("Accepted!")
  else:
    st.write("Rejected!!!")

