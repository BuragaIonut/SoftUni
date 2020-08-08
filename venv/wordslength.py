# result = [print(f"{word for word in input().split(', ')} -> {len(word) for word in input().split(', ')}")]

print(*[f'{word} -> {len(word)}' for word in input().split(', ')], sep = ', ')