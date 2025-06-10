def main(fields: dict) -> int:
    return (
        fields['P1']
        | (fields['P2'] << 7)
        | (fields['P3'] << 11)
        | (fields['P4'] << 19)
        | (fields['P5'] << 21)
        | (fields['P6'] << 28)
    )

print(main({'P1': 109, 'P2': 11, 'P3': 45, 'P4': 3, 'P5': 126, 'P6': 813}))
