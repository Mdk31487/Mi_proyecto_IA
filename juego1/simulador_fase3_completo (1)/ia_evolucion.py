def evolucionar_mentor(mentor):
    mentor.experiencia += 5
    if mentor.experiencia >= 20:
        mentor.nivel += 1
        mentor.experiencia = 0