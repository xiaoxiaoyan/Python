from __future__ import  print_function


def display_inventory(inventory):
    total = 0
    for k, v in inventory.iteritems():
        total += v
    print("total totalber of items is: {0}" .format(total))


def add_to_inventory(inventory,added_items):
    for item in added_items:
        inventory.setdefault(item,0)
        inventory[item] += 1
    return inventory


def main():
    inv = {'arrow': 12, 'dagger': 1, 'gold coin': 42, 'rope': 1, 'torch': 6}
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    display_inventory(inv)
    new_inv = add_to_inventory(inv,dragon_loot)
    display_inventory(new_inv)


if __name__ == "__main__":
    main()
