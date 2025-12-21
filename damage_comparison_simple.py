import matplotlib.pyplot as plt
import numpy as np

# PnP Parameter - realistisch nach neuen Regeln (Base ÷ 100 × Level)
attack_powers = [1, 2, 3, 4, 5, 6]  # A-Pow (Attacke-Power ÷ 20)
test_pnp_level = 10

# Szenarien - realistischer Stat-Bereich mit neuer Formel (Base ÷ 100 × Level)
# Level 10 Pokemon: Stats etwa 4-13 (Base Stats 40-130)
scenarios = {
    'High A, Low D': (7, 3),
    'Ausgeglichen': (5, 5), 
    'Kleine Differenz': (5, 4),
    'High D, Low A': (3, 7)
}

def damage_division(pnp_level, a_pow, attack, defense):
    """PnP-Level × A-Pow × (A ÷ D)"""
    return pnp_level * a_pow * (attack / defense)

def damage_subtraction(pnp_level, a_pow, attack, defense):
    """PnP-Level × A-Pow × (A - D + 1)"""
    return pnp_level * a_pow * max(1, attack - defense + 1)

# Erstelle Vergleichsdiagramm
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Schadensvergleich: Division vs. Subtraktion', fontsize=14)

for idx, (scenario_name, (attack, defense)) in enumerate(scenarios.items()):
    row = idx // 2
    col = idx % 2
    ax = axes[row, col]
    
    division_damages = []
    subtraction_damages = []
    
    for a_pow in attack_powers:
        div_damage = damage_division(test_pnp_level, a_pow, attack, defense)
        sub_damage = damage_subtraction(test_pnp_level, a_pow, attack, defense)
        
        division_damages.append(div_damage)
        subtraction_damages.append(sub_damage)
    
    ax.plot(attack_powers, division_damages, 'r-o', label='Division A/D', linewidth=2)
    ax.plot(attack_powers, subtraction_damages, 'b-s', label='Subtraktion A-D+1', linewidth=2)
    
    ax.set_xlabel('Attackenstärke')
    ax.set_ylabel('Schaden')
    ax.set_title(f'{scenario_name}\nA={attack}, D={defense}')
    ax.legend()
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('damage_comparison.png', dpi=300, bbox_inches='tight')

# Fehleranalyse
print("=== Fehleranalyse: Division vs. Subtraktion ===")
print(f"Test PnP-Level: {test_pnp_level}")
print()

for scenario_name, (attack, defense) in scenarios.items():
    print(f"=== {scenario_name} (A={attack}, D={defense}) ===")
    
    total_rel_error = 0
    total_abs_error = 0
    
    for a_pow in attack_powers:
        div_damage = damage_division(test_pnp_level, a_pow, attack, defense)
        sub_damage = damage_subtraction(test_pnp_level, a_pow, attack, defense)
        
        rel_error = abs((sub_damage - div_damage) / div_damage * 100) if div_damage != 0 else 0
        abs_error = abs(sub_damage - div_damage)
        
        total_rel_error += rel_error
        total_abs_error += abs_error
        
        print(f"A-Pow {a_pow:2}: Division={div_damage:5.1f}, Subtraktion={sub_damage:3.0f}, Fehler={rel_error:5.1f}%")
    
    avg_rel_error = total_rel_error / len(attack_powers)
    avg_abs_error = total_abs_error / len(attack_powers)
    
    print(f"Durchschnitt: Rel. Fehler={avg_rel_error:.1f}%, Abs. Fehler={avg_abs_error:.1f}")
    print()

plt.show()