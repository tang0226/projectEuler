total = 0
for d1 in range(2):
	for d2 in range(2):
		for d3 in range(2):
			for d4 in range(2):
				for d5 in range(2):
					for d6 in range(2):
						for d7 in range(2):
							for d8 in range(2):
								for d9 in range(2):
									for d10 in range(2):
										for d11 in range(2):
											for d12 in range(2):
												for d13 in range(2):
													for d14 in range(2):
														for d15 in range(2):
															nums = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15]
															if sum(nums) > 7:
																a = 1 / 2
																for i in range(1, len(nums)):
																	if nums[i]:
																		a *= 1 / (i + 2)
																	else:
																		a *= (i + 1) / (i + 2)
																total += a
print(1 // total)