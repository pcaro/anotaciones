"""
Filter feeds by language for i18n subsites.

This plugin ensures that each language's feed only contains articles in that language.
It works alongside the i18n_subsites plugin by filtering articles before the feed is written.
"""

from pelican import signals


def on_get_writer(pelican_obj):
    """Hook into get_writer to filter articles before feeds are written."""
    from pelican.writers import Writer
    
    # Get the original Writer class methods
    original_write_feed = Writer.write_feed
    original_init = Writer.__init__
    
    # Store the output path when Writer is initialized
    def patched_init(self, output_path, settings=None):
        self._i18n_output_path = output_path
        return original_init(self, output_path, settings=settings)
    
    Writer.__init__ = patched_init
    
    def filtered_write_feed(self, elements, context, path=None, url=None, feed_type='atom', override_output=False, feed_title=None):
        """Wrapper that filters elements by language before writing."""
        if elements and len(elements) > 0:
            # Determine language from output path
            # Main site (Spanish): output_path ends with 'output_dev' or similar
            # English subsite: output_path ends with 'en' (output_dev/en)
            output_path = getattr(self, '_i18n_output_path', '')
            
            # Check if we're in the English subsite
            import os
            output_dir = os.path.basename(output_path.rstrip('/'))
            if output_dir == 'en':
                current_lang = 'en'
            else:
                current_lang = 'es'  # Default to Spanish for main site
            
            # Filter articles by language
            original_count = len(elements)
            filtered_elements = [e for e in elements if getattr(e, 'lang', None) == current_lang]
            
            if len(filtered_elements) != original_count:
                elements = filtered_elements
        
        # Call original with filtered elements
        return original_write_feed(self, elements, context, path=path, url=url, feed_type=feed_type, override_output=override_output, feed_title=feed_title)
    
    Writer.write_feed = filtered_write_feed


def register():
    signals.get_writer.connect(on_get_writer)