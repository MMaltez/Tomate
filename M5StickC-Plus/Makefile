# Makefile
TARGETS=note1.html
.PHONY: all clean

all: $(TARGETS)

clean:
	$(RM) $(TARGETS)

%.html : %.md
	pandoc -s -c dark.css $< -o $@
