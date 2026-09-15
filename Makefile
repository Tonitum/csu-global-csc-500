module%.docx: modules/module%/report.md
	pandoc --from=markdown --to=docx --output="$@" "$<"

.PRECIOUS: module%.docx

module%: module%.docx
	@:

.PHONY: clean

clean:
	find . -name "module*.docx" -delete
