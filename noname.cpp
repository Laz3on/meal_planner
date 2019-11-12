///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Jul 28 2019)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "noname.h"

///////////////////////////////////////////////////////////////////////////

MyWizard1::MyWizard1( wxWindow* parent, wxWindowID id, const wxString& title, const wxBitmap& bitmap, const wxPoint& pos, long style )
{
	this->Create( parent, id, title, bitmap, pos, style );
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );

	wxWizardPageSimple* m_wizPage1 = new wxWizardPageSimple( this );
	m_pages.Add( m_wizPage1 );


	this->Centre( wxBOTH );

	for ( unsigned int i = 1; i < m_pages.GetCount(); i++ )
	{
		m_pages.Item( i )->SetPrev( m_pages.Item( i - 1 ) );
		m_pages.Item( i - 1 )->SetNext( m_pages.Item( i ) );
	}
}

MyWizard1::~MyWizard1()
{
	m_pages.Clear();
}
