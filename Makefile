module%.docx: modules/module%/report.md
	pandoc --from=markdown --to=docx --reference-doc=reference.docx --output="$@" "$<"

.PRECIOUS: module%.docx

module%: module%.docx
	@:

new-module:
	echo foo
	mkdir -p modules/module$(MODULE_NUMBER)
	cp -r templates/* modules/module$(MODULE_NUMBER)/
	sed -i '' 's/MODULE_NUMBER/$(MODULE_NUMBER)/g' modules/module$(MODULE_NUMBER)/*.py
	sed -i '' 's/MODULE_NUMBER/$(MODULE_NUMBER)/g' modules/module$(MODULE_NUMBER)/*.md

.PHONY: clean

clean:
	find . -name "module*.docx" -delete
