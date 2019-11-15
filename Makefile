override CXXFLAGS += -std=c++14 -Weverything -Wno-c++98-compat\
-Wno-shadow-field-in-constructor -Wno-shadow -Wno-padded

DSL_2_C:
run: $(TARGET)
	LD_LIBRARY_PATH=/usr/local/gcc/lib/gcc/x86_64-pc-linux-gnu/9.2.0/../../../../lib64 \
	./$(TARGET)
